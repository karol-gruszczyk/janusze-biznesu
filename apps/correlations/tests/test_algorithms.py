from datetime import datetime, timedelta

import pytest

from apps.correlations.algorithms import CorrelationAlgorithm, PearsonCorrelation
from apps.shares.models import Share, ShareRecord
from apps.gains.models import Gain


@pytest.fixture(scope='session')
def init_db():
    in_share1 = Share.objects.create(name='in_test_share1')
    in_share2 = Share.objects.create(name='in_test_share2')
    out_share = Share.objects.create(name='out_test_share')
    for share in (in_share1, in_share2, out_share):
        for i in range(10):
            ShareRecord.objects.create(share=share, date=datetime.now().date() - timedelta(days=i),
                                       open=0, close=0, high=0, low=0, volume=0)
    for share in [in_share1, in_share2, out_share]:
        records = list(share.records.all())
        for lower_record, upper_record in zip(records[:-1], records[1:]):
            Gain.objects.create(share=share, date=upper_record.date,
                                lower_record=lower_record, upper_record=upper_record,
                                volume_gain=0, open_gain=0, close_gain=0, high_gain=0, low_gain=0)


@pytest.mark.django_db
class TestCorrelationAlgorithm:

    def test_algorithm_init(self, init_db):
        in_share1 = Share.objects.get(name='in_test_share1')
        in_share2 = Share.objects.get(name='in_test_share2')
        out_share = Share.objects.get(name='out_test_share')
        alg = CorrelationAlgorithm([in_share1, in_share2], out_share, 1, "2010-01-01")
        assert len(alg.output_records) == 8
        for share, records in alg.input_records.items():
            assert len(records) == len(alg.output_records)


@pytest.mark.django_db
class TestPearsonCorrelation:

    def test_one_to_one_correlation(self, init_db):
        pass

    def test_many_to_one_correlation(self, init_db):
        pass
