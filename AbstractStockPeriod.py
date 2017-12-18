from abc import ABC, abstractmethod


class AbstractStockPeriod(ABC):
    def __init__(self, stock):
        self._stock_day_list = list()
        self._stock_day_list.append(stock)

    def average(self):
        numerator = 0
        denominator = 0

        for s in self._stock_day_list:
            numerator += s.volume * s.adjusted_close
            denominator += s.volume

        return numerator / denominator

    @abstractmethod
    def add_stock_day(self, stock):
        pass

    @property
    def stock_day_list(self):
        return self._stock_day_list
