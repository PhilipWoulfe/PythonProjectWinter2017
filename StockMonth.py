from StockYear import StockYear


class StockMonth(StockYear):
    def __init__(self, stock):
        """
        Overrides the default implementation
        Create a new Stock month object with the year and month of the stock object passed to the constructor
        :param stock: Used to determine the StockMonth year and month fielda
        """
        super(StockMonth, self).__init__(stock)
        self._month = stock.stock_date.month

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.month == other.month and super(StockMonth, self).__eq__(other)
        return NotImplemented

    def __lt__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.month < other.month and super(StockMonth, self).__lt__(other)
        return NotImplemented

    def __gt__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.month > other.month and super(StockMonth, self).__gt__(other)
        return NotImplemented

    def __le__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.month <= other.month and super(StockMonth, self).__le__(other)
        return NotImplemented

    def __ge__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.month >= other.month and super(StockMonth, self).__ge__(other)
        return NotImplemented

    def add_stock_day(self, stock):
        """
        Overrides the abstract implementation
        Add StockDay item to stock_day_list
        :param stock: StockDay object to be added to stock_day_list
        Discard if StockDay and StockMonth year and month properties don't match
        """
        if stock.stock_date.month == self.month:
            super(StockMonth, self).add_stock_day(stock)
        else:
            print("Invalid month - stock not added")

    @property
    def month(self):
        """Get stock month"""
        return self._month
