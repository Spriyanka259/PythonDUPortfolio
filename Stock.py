"""
Author: Priyanka Sirigadde
Date created: 08/06/20
Functionality: This program consists of Stock class to initialize stock object.
"""

import json
import csv
from datetime import datetime
import DBConnection


class Stock:
    def __init__(self, symbol, date, open_price, high, low, closing_price, volume):
        """Initializing the Stock class"""
        self.symbol = symbol
        self.date = date
        self.open_price = open_price
        self.high = high
        self.low = low
        self.closing_price = closing_price
        self.volume = volume
        self.closePriceList = []
        self.dateList = []
        self.stocks = {}
        self.stock_value_list = []
        self.stock_list = []

    def add_lists(self, closing_price, date):
        """This function is to append close price and dates to lists"""
        self.closePriceList.append(closing_price)
        self.dateList.append(date)
        return self.closePriceList

    def read_csv_file(self):
        """This function reads CSV file and the data residing in it"""
        try:
            with open('Lesson6_Data_Stocks.csv', 'r') as stock_file:
                reader = csv.reader(stock_file)
                next(reader)
                for row in reader:
                    self.stocks[row[0]] = {'NO_SHARES': row[1]}
        except FileNotFoundError as e:
            print('File not found at the given location, Check the Path!')
        return self.stocks

    def add_to_dict(self, stock_dict, close_price_dict, new_stock):
        """This function reads the json file and loads the data into dictionary"""
        try:
            with open('AllStocks.json', 'r') as json_file:
                json_data = json.load(json_file)

            for each in json_data:
                new_stock = Stock(each['Symbol'], each['Date'], each['Open'], each['High'], each['Low'],
                                  each['Close'], each['Volume'])
                self.stock_list.append(new_stock)
                if each['Symbol'] not in stock_dict:
                    stock_dict[each['Symbol']] = new_stock
                else:
                    stock_dict[each['Symbol']].date = each['Date']
                for stock in self.stocks:
                    if each['Symbol'] == stock:
                        self.closePriceList = stock_dict[each['Symbol']].add_lists(each['Close'],
                                                                                   datetime.strptime(each['Date'],
                                                                                                     '%d-%b-%y'))
                        close_price_dict[each['Symbol']] = self.closePriceList
        except Exception as e:
            print('Exception while reading json data', e)
        return close_price_dict, stock_dict, self.stock_list

    def calculate_graph_value(self, graph_dict, close_price_dict):
        """This function helps in creating the lists for graphing libraries to handle"""
        try:
            for key, value in close_price_dict.items():
                for stock, quantity in self.stocks.items():
                    if key == stock:
                        self.stock_value_list = [element * float(quantity['NO_SHARES']) for element in value]
                        graph_dict[stock] = self.stock_value_list
        except Exception as e:
            print('Failure while adding stocks to a list', e)
        return graph_dict

    def insert_into_db(self, stock_list, i):
        """This function inserts the data of json file containing stock prices into the ict4370 database"""
        try:
            connection, cursor = DBConnection.db_connection()
            for stock in stock_list:
                sqlite_insert_query = """INSERT INTO Stock(id, symbol, open_price, highest_price, lowest_price,
                                closing_price, purchase_date, volume) values (?, ?, ?, ?, ?, ?, ?, ?) """
                count = cursor.execute(sqlite_insert_query, (i, stock.symbol, stock.open_price, stock.high,
                                                             stock.low, stock.closing_price, stock.date, stock.volume))
                i = i + 1
            DBConnection.db_execution()
        except Exception as e:
            print('Insertion of Stock failed due to:', e)



