from abc import ABC, abstractmethod

class InstrumentProcessor(ABC):
    @abstractmethod
    def add_entry(self, date, value):
        pass

    @abstractmethod
    def result(self):
        pass

class InstrumentProcessorFactory:
    @staticmethod
    def create(name):
        if name == "INSTRUMENT1":
            from .instrument1 import Instrument1Processor
            return Instrument1Processor()
        elif name == "INSTRUMENT2":
            from .instrument2 import Instrument2Processor
            return Instrument2Processor()
        elif name == "INSTRUMENT3":
            from .instrument3 import Instrument3Processor
            return Instrument3Processor()
        else:
            from .generic import GenericInstrumentProcessor
            return GenericInstrumentProcessor()
