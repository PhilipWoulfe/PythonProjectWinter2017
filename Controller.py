import ReadFromCsv
from StockMonth import StockMonth
from StockYear import StockYear
from typing import TypeVar

T = TypeVar("T")


def main():
    stock = ReadFromCsv.ReadFromCsv.csv_to_stockday_list()  # Read data from csv

    stock_month = get_stock(stock, StockMonth)  # create stock month list
    stock_year = get_stock(stock, StockYear)  # create stock year list

    print_three(stock_month, StockMonth, True)  # print top 3 stock months
    print_three(stock_month, StockMonth, False)  # print bottom 3 stock months

    print_three(stock_year, StockYear, True)  # print top 3 stock years
    print_three(stock_year, StockYear, False)  # print bottom 3 stock years


def get_stock(stock, t: T):
    """
    Create stock period object list and assign stock days to appropriate object
    :param stock: list of StockDays
    :param t: Type of AbstractStockPeriod object required
    :return: list of AbstractStockPeriod objects determined by T
    """
    stock_list = list()

    for s in stock:
        tmp = t(s)  # create new object of type T
        if tmp in stock_list:           # if the object of type T exists in ist already
            i = stock_list.index(tmp)       # get index of the object
            stock_list[i].add_stock_day(s)  # and add StockDay object to that AbstractStockPeriod
        else:                           # otherwise
            stock_list.append(tmp)          # add the newly created AbstractStockPeriod to the stock list

    return stock_list


def print_three(stock, t: T, is_top):
    """
    Print three AbstractStockPeriod objects determined by T and is_top
    :param stock: list of AbstractStockPeriod objects
    :param t: Generic type - determines how AbstractStockPeriod will be printed
    :param is_top: Boolean - Print top 3 if True or Bottom 3 otherwise
    """
    rank = 'Top' if is_top else 'Bottom'  # set title based on is_top parameter

    # Sort stock list based on the average in order depending on is_top parameter
    stock = sorted(stock, key=lambda x: x.average(), reverse=is_top)

    # display determined by type of generic T
    if t == StockMonth:
        print_months(stock[0:3], rank)  # print first 3 items in list
    elif t == StockYear:
        print_years(stock[0:3], rank)  # print first 3 items in list


def print_months(stock, rank):
    """
    Print values for list of StockMonth objects
    :param stock: list of StockMonth objects
    :param rank: String - usually set to top or bottom
    """
    print(' ___________________________ ')
    print('|    %6s 3 Months        |' % rank)
    print('|___________________________|')
    print('|%6s |%6s |%10s |' % ('Year', 'Month', 'Average'))
    print('|_______|_______|___________|')
    for s in stock:
        print('|%6d |%6d |%10.2f |' % (s.year, s.month, s.average()))
    print('|_______|_______|___________|')


def print_years(stock, rank):
    """
    Print values for list of StockYear objects
    :param stock: list of StockYear objects
    :param rank: String - usually set to top or bottom
    """
    print(' ___________________________ ')
    print('|    %6s 3 Years         |' % rank)
    print('|___________________________|')
    print('|%9s | %14s |' % ('Year', 'Average'))
    print('|__________|________________|')
    for s in stock:
        print('|%9d | %14.2f |' % (s.year, s.average()))
    print('|__________|________________|')


if __name__ == '__main__':
    main()
