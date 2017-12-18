from AbstractStockPeriod import AbstractStockPeriod


class StockYear(AbstractStockPeriod):

    def __init__(self, stock):
        """
        Overrides the default implementation
        Create a new Stock year object with the year of the stock object passed to the constructor
        :param stock: Used to determine the StockYear year field
        """
        super(StockYear, self).__init__(stock)
        self._year = stock.stock_date.year

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

    def add_stock_day(self, stock):
        """
        Overrides the abstract implementation
        Add StockDay item to stock_day_list
        :param stock: StockDay object to be added to stock_day_list
        Discard if StockDay and StockYear year property don't match
        """
        if stock.stock_date.year == self.year:
            self._stock_day_list.append(stock)
            self._stock_day_list.sort()
        else:
            print("Invalid year - stock not added")

    @property
    def year(self):
        """Get stock year"""
        return self._year
