from .base import InstrumentProcessor
#For INSTRUMENT2 – mean for November 2014
class Instrument2Processor(InstrumentProcessor):
    def __init__(self):
        self.total = 0.0
        self.count = 0

    def add_entry(self, date, value):
        if date.month == 11 and date.year == 2014:
            self.total += value
            self.count += 1

    def result(self):
        return round(self.total / self.count, 4) if self.count else None
