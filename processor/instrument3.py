from .base import InstrumentProcessor

#For INSTRUMENT3 – any other statistical calculation that we can compute "on-the-fly" as we read the file (it's up to you)
class Instrument3Processor(InstrumentProcessor):
    def __init__(self):
        self.min_val = float('inf')
#calculating minimum
    def add_entry(self, date, value):
        if value < self.min_val:
            self.min_val = value

    def result(self):
        return self.min_val if self.min_val != float('inf') else None
