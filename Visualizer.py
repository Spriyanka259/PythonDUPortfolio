import Stock
import DataVisualize
import DBConnection


def main():
    stock_dict = {}
    close_price_dict = {}
    graph_dict = {}
    # DBConnection.create_tables()# I called this only once to create tables at the beginning
    stock_instance = Stock.Stock(symbol='', date='', open_price='', high='', low='', closing_price='', volume='')
    stock_instance.read_csv_file()
    close_price_dict, stock_dict, stock_list = stock_instance.add_to_dict(stock_dict, close_price_dict, stock_instance)
    graph_dict = stock_instance.calculate_graph_value(graph_dict, close_price_dict)
    stock_instance.insert_into_db(stock_list, i=1)
    DataVisualize.visualize_line(graph_dict, stock_dict)


if __name__ == "__main__":
    """This if statement runs the function if the name is main"""
    main()
