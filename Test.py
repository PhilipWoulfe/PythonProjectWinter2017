import ReadFromCsv
from StockMonth import StockMonth
from StockYear import StockYear
from typing import TypeVar

T = TypeVar("T")


def main():
    stock = ReadFromCsv.ReadFromCsv.csv_to_stockday_list()

    stock_month = get_stock(stock, StockMonth)
    stock_year = get_stock(stock, StockYear)

    for e in stock_month:
        print(e.year, e.month, e.average())

    print('_____________')

    for e in stock_year:
        print(e.year, e.average())


def get_stock(stock, t: T):
    stock_list = list()
    for s in stock:
        tmp = t(s)
        if tmp in stock_list:
            i = stock_list.index(tmp)
            stock_list[i].add_stock_day(s)
        else:
            stock_list.append(tmp)

    # Sort stock list based on the average in descending order
    stock_list.sort(key=lambda x: x.average(), reverse=True)
    return stock_list


if __name__ == '__main__':
    main()
