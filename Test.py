import ReadFromCsv
from StockMonth import StockMonth
from StockYear import StockYear
from typing import TypeVar

T = TypeVar("T")


def main():
    stock = ReadFromCsv.ReadFromCsv.csv_to_stockday_list()

    stock_month = get_stock(stock, StockMonth)
    stock_year = get_stock(stock, StockYear)

    print_top_three(stock_month, StockMonth)
    print_bottom_three(stock_month, StockMonth)

    print_top_three(stock_year, StockYear)
    print_bottom_three(stock_year, StockYear)


def get_stock(stock, t: T):
    stock_list = list()
    for s in stock:
        tmp = t(s)
        if tmp in stock_list:
            i = stock_list.index(tmp)
            stock_list[i].add_stock_day(s)
        else:
            stock_list.append(tmp)

    return stock_list


def print_top_three(stock, t: T):
    # Sort stock list based on the average in descending order
    stock = sorted(stock, key=lambda x: x.average(), reverse=True)

    if t == StockMonth:
        print_months(stock[0:3], 'Top')
    elif t == StockYear:
        print_years(stock[0:3], 'Top')


def print_bottom_three(stock, t: T):
    # Sort stock list based on the average in ascending order
    stock = sorted(stock, key=lambda x: x.average())

    if t == StockMonth:
        print_months(stock[0:3], 'Bottom')
    elif t == StockYear:
        print_years(stock[0:3], 'Bottom')


def print_months(stock, str):
    print(' ___________________________ ')
    print('|    %6s 3 Months        |' % str)
    print('|___________________________|')
    print('|%6s |%6s |%10s |' % ('Year', 'Month', 'Average'))
    print('|_______|_______|___________|')
    for s in stock[0:3]:
        print('|%6d |%6d |%10.2f |' % (s.year, s.month, s.average()))
    print('|_______|_______|___________|')


def print_years(stock, str):
    print(' ___________________________ ')
    print('|    %6s 3 Years         |' % str)
    print('|___________________________|')
    print('|%9s | %14s |' % ('Year', 'Average'))
    print('|__________|________________|')
    for s in stock[0:3]:
        print('|%9d | %14.2f |' % (s.year, s.average()))
    print('|__________|________________|')


if __name__ == '__main__':
    main()
