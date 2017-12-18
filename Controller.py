import ReadFromCsv
from StockMonth import StockMonth
from StockYear import StockYear
from typing import TypeVar

T = TypeVar("T")


def main():
    number_of_stock_to_print = 6

    stock = ReadFromCsv.ReadFromCsv.csv_to_stockday_list()  # Read data from csv

    stock_month = get_stock(stock, StockMonth)  # create stock month list
    stock_year = get_stock(stock, StockYear)  # create stock year list

    print_n_stock(stock_month, StockMonth, True, number_of_stock_to_print)  # print top 6 stock months
    print_n_stock(stock_month, StockMonth, False, number_of_stock_to_print)  # print bottom 6 stock months

    print_n_stock(stock_year, StockYear, True, number_of_stock_to_print)  # print top 6 stock years
    print_n_stock(stock_year, StockYear, False, number_of_stock_to_print)  # print bottom 6 stock years


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


def print_n_stock(stock, t: T, is_top, n):
    """
    Print three AbstractStockPeriod objects determined by T and is_top
    :param stock: list of AbstractStockPeriod objects
    :param t: Generic type - determines how AbstractStockPeriod will be printed
    :param is_top: Boolean - Print top 3 if True or Bottom 3 otherwise
    :param n: number of AbstractStockPeriod objects to print
    """
    rank = 'Top' if is_top else 'Bottom'  # set title based on is_top parameter

    # Sort stock list based on the average in order depending on is_top parameter
    stock = sorted(stock, key=lambda x: x.average(), reverse=is_top)

    # display determined by type of generic T
    if t == StockMonth:
        print_months(stock[0:n], rank, n)  # print first 6 items in list
    elif t == StockYear:
        print_years(stock[0:n], rank, n)  # print first 6 items in list


def print_months(stock, rank, n):
    """
    Print values for list of StockMonth objects
    :param stock: list of StockMonth objects
    :param rank: String - usually set to top or bottom
    :param n: number of months to print
    """
    print(' ___________________________ ')
    print('|    %6s %d Months        |' % (rank, n))
    print('|___________________________|')
    print('|%6s |%6s |%10s |' % ('Year', 'Month', 'Average'))
    print('|_______|_______|___________|')
    for s in stock:
        print('|%6d |%6d |%10.2f |' % (s.year, s.month, s.average()))
    print('|_______|_______|___________|')


def print_years(stock, rank, n):
    """
    Print values for list of StockYear objects
    :param stock: list of StockYear objects
    :param rank: String - usually set to top or bottom
    :param n: number of years to print
    """
    print(' ___________________________ ')
    print('|    %6s %d Years         |' % (rank, n))
    print('|___________________________|')
    print('|%9s | %14s |' % ('Year', 'Average'))
    print('|__________|________________|')
    for s in stock:
        print('|%9d | %14.2f |' % (s.year, s.average()))
    print('|__________|________________|')


if __name__ == '__main__':
    main()
