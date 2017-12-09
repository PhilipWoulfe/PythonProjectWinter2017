import ReadFromCsv
from datetime import datetime

#print(datetime.strptime('2004-09-09', '%Y-%M-%d'))

stock = ReadFromCsv.ReadFromCsv.csv_to_stockday_list()

print(stock[0].stock_date)

