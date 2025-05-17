from .base import InstrumentProcessor
import heapq

class GenericInstrumentProcessor(InstrumentProcessor):
    def __init__(self):
        self.latest = []

    def add_entry(self, date, value):
        # timestamp removing the oldest date
        #heapq -min heap removing min element
        heapq.heappush(self.latest, (date.timestamp(), value))
        if len(self.latest) > 10:
            heapq.heappop(self.latest)

    def result(self):
        return round(sum(v for _, v in self.latest), 4)



        # def __init__(self):
        #     self.entries = []  #  (date, value)
        #
        # def add_entry(self, date, value):
        #     self.entries.append((date, value))
        #
        # def result(self):
        #
        #     self.entries.sort(key=lambda x: x[0], reverse=True)
        #     # 10 latest
        #     top_10 = self.entries[:10]
        #     # sum
        #     return round(sum(value for _, value in top_10), 4)

