from StockYear import StockYear


class StockMonth(StockYear):
    def __init__(self, stock):
        super(StockMonth, self).__init__(stock)
        self._month = stock.stock_date.month

    def add_stock_day(self, stock):
        """Overrides the abstract implementation"""
        if stock.stock_date.month == self.month:
            super(StockMonth, self).add_stock_day(stock)
        else:
            print("Invalid month - stock not added")

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

    @property
    def month(self):
        return self._month
