from typing import Dict, List, Tuple
from datetime import date
from itertools import combinations
from collections import namedtuple

import numpy as np

from apps.shares.models import Share


SimpleShare = namedtuple("SimpleShare", "name records")


class CorrelationSetGenerator:
    shares_as_input = Dict[str, np.array]
    shares_as_output = Dict[str, np.array]
    max_set_length = None

    def __init__(self, shares: List[Share], day_interval: int, from_date: date, max_set_length: int):
        self.max_set_length = max_set_length
        share_records = {share.name: share.records.filter(date__gte=date) for share in shares}
        min_length = min(*[share.count() for share in share_records.values()])
        for key in share_records:
            share_records[key] = share_records[key][len(share_records[key]) - min_length:]
        self.shares_as_input = {share: np.array(records[:-day_interval]) for share, records in share_records.items()}
        self.shares_as_input = {share: np.array(records[day_interval:]) for share, records in share_records.items()}

    def sets(self) -> Tuple[Tuple[list], list]:
        for i in range(self.max_set_length):
            for in_share_combination in combinations(self.shares_as_input.keys(), i):
                for out_share in self.shares_as_output.keys():
                    if out_share in in_share_combination:
                        continue
                    yield ((SimpleShare(name=share, records=self.shares_as_input[share])
                            for share in in_share_combination),
                           SimpleShare(name=out_share, records=self.shares_as_output[out_share]))
