from datetime import datetime


class StockDay(object):
    def __init__(self, stock_date, open_value, high, low, close, adjusted_close, volume):
        """
        Create a StockDay object
        :param stock_date: date for Stock values
        :param open_value: opening value of the stock on date
        :param high: highest value of the stock on date
        :param low: lowest value of stock on date
        :param close: closing value of stock on date
        :param adjusted_close: adjusted closing value of stock on date
        :param volume: volume of stock traded on date
        """
        self._stock_date = datetime.strptime(stock_date, '%Y-%m-%d').date()
        self._open_value = float(open_value)
        self._high = float(high)
        self._low = float(low)
        self._close = float(close)
        self._adjusted_close = float(adjusted_close)
        self._volume = int(volume)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.stock_date == other.stock_date
        return NotImplemented

    def __lt__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.stock_date < other.stock_date
        return NotImplemented

    def __gt__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.stock_date > other.stock_date
        return NotImplemented

    def __le__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.stock_date <= other.stock_date
        return NotImplemented

    def __ge__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.stock_date >= other.stock_date
        return NotImplemented

    @property
    def stock_date(self):
        """Get the stock date"""
        return self._stock_date

    @property
    def open_value(self):
        """Get the opening value for the stock"""
        return self._open_value

    @property
    def high(self):
        """Return the stock's highest values for the date"""
        return self._high

    @property
    def low(self):
        """Return the stock's lowest value for the date"""
        return self._low

    @property
    def close(self):
        """Get the stocks closing value for the date"""
        return self._close

    @property
    def adjusted_close(self):
        """Get the Stocks adjusted closing value for the date"""
        return self._adjusted_close

    @property
    def volume(self):
        """Get the stocks volume for the date"""
        return self._volume
