from abc import ABC, abstractmethod


class AbstractStockPeriod(ABC):
    def __init__(self, stock):
        """
        Instantiate Stock Period and assign stock to stock_day_list
        :param stock: a single StockDay object
        """
        self._stock_day_list = list()
        self._stock_day_list.append(stock)

    @abstractmethod
    def add_stock_day(self, stock):
        pass

    def average(self):
        """
        Determines the average price of the StockDay objects in the stock_day_list
        :return: Floating Point average of stock prices
        """
        numerator = 0
        denominator = 0

        # get numerator and denominator for calculating stock average
        for s in self._stock_day_list:
            numerator += s.volume * s.adjusted_close
            denominator += s.volume

        # calculate stock average
        return numerator / denominator

    @property
    def stock_day_list(self):
        """Get stock day list"""
        return self._stock_day_list
