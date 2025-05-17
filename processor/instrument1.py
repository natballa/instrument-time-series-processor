from .base import InstrumentProcessor
#For INSTRUMENT1 – mean
class Instrument1Processor(InstrumentProcessor):
    def __init__(self):
        self.total = 0.0
        self.count = 0

    def add_entry(self, date, value):
        self.total += value
        self.count += 1

    def result(self):
        return round(self.total / self.count, 4) if self.count else None
