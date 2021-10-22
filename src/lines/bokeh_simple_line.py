from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import Button

X_AXIS = Y_AXIS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

main_plot = figure(width=900, height=900)
main_line = main_plot.line(x=X_AXIS, y=Y_AXIS, line_width=2, color='red')
data_source = main_line.data_source


def handler_main_plot(event):
    new_data = dict()
    new_data['x'] = data_source.data['x'] + [random() * 2021]
    new_data['y'] = data_source.data['y'] + [random() * 2021]
    data_source.data = new_data


# add a button widget and set the handler to be called on click
main_button = Button(label="Click Here")
main_button.on_click(handler_main_plot)

# configure the root elements in the Document object
curdoc().add_root(column(main_plot, main_button))

# run the following command from terminal
# bokeh serve bokeh_simple_line.py --show
