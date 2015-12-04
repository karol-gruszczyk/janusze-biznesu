from datetime import date
from typing import List, Tuple

from scipy.stats import pearsonr
from celery import task

from apps.shares.models import ShareSet
from .correlation_set import SimpleShare


class CorrelationAlgorithm:
    input_shares = List[SimpleShare]
    output_share = None

    def __init__(self, correlation_set: Tuple[Tuple[SimpleShare], SimpleShare]):
        self.input_shares = correlation_set[0]
        self.output_share = correlation_set[1]

    def get_correlation(self) -> float:
        raise NotImplementedError('\'CorrelationAlgorithm\' is abstract. You should implement your own method')


class PearsonCorrelation(CorrelationAlgorithm):

    def get_correlation(self) -> float:
        if len(self.input_shares) == 1:
            return pearsonr(self.input_shares[0].records, self.output_share.records)
        return NotImplementedError('A many to one correlation isn\'t implemented yet')


@task
def process_pearson_correlation(shares: ShareSet, day_interval: int, start_date: date, max_set_length: int) -> None:
    pass
