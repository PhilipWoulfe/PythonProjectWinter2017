import csv
import tkinter as tk
from tkinter import filedialog
from StockDay import StockDay


class ReadFromCsv(object):

    @staticmethod
    def csv_to_stockday_list():
        """
        Generate a list of StockDay objects from a user selected csv file
        :return: list of StockDay objects
        """
        root = tk.Tk()
        root.withdraw()

        # You can find the file yourself to save me the hassle... :P
        csv_path = filedialog.askopenfilename()

        stockday_list = list()

        with open(csv_path, newline='') as csv_file:
            first_line = True

            csv_reader = csv.reader(csv_file, delimiter=',')  # read csv and separate on ","

            for row in csv_reader:
                if first_line:  # skip first line since it's the titles
                    first_line = False
                    continue

                # check for missing or extra entries in the csv
                if len(row) != 7:
                    continue

                stock = None

                # Create fields for new StockDay object
                stock_date = row[0]
                stock_open = row[1]
                stock_high = row[2]
                stock_low = row[3]
                stock_close = row[4]
                stock_adj_close = row[5]
                stock_volume = row[6]

                # try to create new StockDay object
                try:
                    stock = StockDay(
                        stock_date
                        , stock_open
                        , stock_high
                        , stock_low
                        , stock_close
                        , stock_adj_close
                        , stock_volume
                    )

                except ValueError as verr:
                    print(verr)

                # Ensure object was created
                if stock is not None:
                    stockday_list.append(stock)

        return stockday_list
