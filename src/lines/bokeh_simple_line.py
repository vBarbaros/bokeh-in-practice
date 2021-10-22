from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import Button

X_AXIS = Y_AXIS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

main_plot = figure(width=900, height=900)
l = main_plot.line(x=X_AXIS, y=Y_AXIS, line_width=2, color='red')
ds = l.data_source


def handler_main_plot(event):
    new_data = dict()
    new_data['x'] = ds.data['x'] + [random() * 2021]
    new_data['y'] = ds.data['y'] + [random() * 2021]
    ds.data = new_data


# add a button widget and configure with the call back
button = Button(label="Click Here")
button.on_click(handler_main_plot)

curdoc().add_root(column(main_plot, button))
# bokeh serve bokeh_simple_line.py --show
