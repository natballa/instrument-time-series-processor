from datetime import datetime
from processor.instrument1 import Instrument1Processor
from processor.instrument2 import Instrument2Processor
from processor.instrument3 import Instrument3Processor
from processor.generic import GenericInstrumentProcessor

def test_instrument1_mean():
    p = Instrument1Processor()
    p.add_entry(datetime(2024, 1, 1), 10)
    p.add_entry(datetime(2024, 1, 2), 20)
    assert p.result() == 15.0

def test_instrument2_mean_nov2014():
    p = Instrument2Processor()
    p.add_entry(datetime(2014, 11, 1), 100)
    p.add_entry(datetime(2014, 11, 15), 200)
    p.add_entry(datetime(2015, 1, 1), 999)  # the date to be ignored
    assert p.result() == 150.0

def test_instrument3_min():
    p = Instrument3Processor()
    p.add_entry(datetime(2023, 1, 1), 5)
    p.add_entry(datetime(2023, 1, 2), 3)
    p.add_entry(datetime(2023, 1, 3), 8)
    assert p.result() == 3

def test_generic_sum_latest_10():
    p = GenericInstrumentProcessor()
    for i in range(15):
        p.add_entry(datetime(2023, 1, i + 1), i + 1)
    assert p.result() == sum(range(6, 16))  # 6+7+...+15 = 105