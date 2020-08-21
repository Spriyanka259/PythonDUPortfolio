"""
Author: Priyanka Sirigadde
Date created: 08/05/20
Functionality: This program styles the line graph using Pygal and visualizes the data provided to it.
"""

import pygal
from pygal.style import Style

custom_style = Style(
    colors=('#0343df', '#e50000', '#ffff14', '#929591', '#E853A0'),
    font_family='Roboto,Helvetica,Arial,sans-serif',
    background='transparent',
    label_font_size=14,
)

c = pygal.Line(
    title='Stock Values',
    style=custom_style,
    y_title='Prices',
    width=1200,
    x_label_rotation=270,
)

c._x_title = 'Date of the Stock'


def visualize_line(graph_dict, stock_dict):
    """This function visualizes the line graph for the stock data"""
    try:
        for each, stock in stock_dict.items():
            c.x_labels = map(lambda d: d.strftime('%d-%b-%y'), stock.dateList)
            for key, value in graph_dict.items():
                if each == key:
                    c.add(each, value)
        c.render_to_file('stocks.svg')
    except Exception as e:
        print('Problem occurred while visualizing the line graph', e)

