from AbstractStockPeriod import AbstractStockPeriod


class StockYear(AbstractStockPeriod):
    def __init__(self, stock):
        super(StockYear, self).__init__(stock)
        self._year = stock.stock_date.year

    def add_stock_day(self, stock):
        """Overrides the abstract implementation"""
        if stock.stock_date.year == self.year:
            self._stock_day_list.append(stock)
            self._stock_day_list.sort()
        else:
            print("Invalid year - stock not added")

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.year == other.year
        return NotImplemented

    def __lt__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.year < other.year
        return NotImplemented

    def __gt__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.year > other.year
        return NotImplemented

    def __le__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.year <= other.year
        return NotImplemented

    def __ge__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.year >= other.year
        return NotImplemented

    @property
    def year(self):
        return self._year
