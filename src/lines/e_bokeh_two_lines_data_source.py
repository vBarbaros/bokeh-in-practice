import math
from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, FixedTicker, ColumnDataSource

X_AXIS = Y_AXIS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

main_plot = figure(
    title='Two separate lines, cos & sin - use random values with DataSource structures ("bokeh-in-practice", November 2021)',
    tools="box_select,box_zoom,lasso_select,reset",
    width=900, height=900)

main_plot.xaxis.axis_label = "Integers (0 through 9)"
main_plot.xaxis.axis_label_text_color = "#aa6666"
main_plot.xaxis.axis_label_standoff = 20
main_plot.xaxis.bounds = (-1, 10)
main_plot.xaxis.ticker = FixedTicker(ticks=X_AXIS)

main_plot.yaxis.axis_label = "Randomly generated (sin vs cos) values stored and used from DataSource"
main_plot.yaxis.axis_label_text_font_style = "italic"

DATA_SOURCE_SINE = ColumnDataSource(data=dict(x_sin=X_AXIS, y_sin=Y_AXIS))
main_line_sin = main_plot.line(x="x_sin", y="y_sin", source=DATA_SOURCE_SINE, line_width=3, color='red',
                               line_dash=[2, 2],
                               legend_label='Random sin() values')
main_cross_sin = main_plot.cross(x="x_sin", y="y_sin", source=DATA_SOURCE_SINE, line_width=3, color='blue',
                                   legend_label='Random sin() values',
                                   size=15)

DATA_SOURCE_COSINE = ColumnDataSource(data=dict(x_cos=X_AXIS, y_cos=Y_AXIS))
main_line_cos = main_plot.line(x="x_cos", y="y_cos", source=DATA_SOURCE_COSINE, line_width=3, color='green',
                               line_dash=[4, 4],
                               legend_label='Random cos() values')
main_triangle_cos = main_plot.triangle(x="x_cos", y="y_cos", source=DATA_SOURCE_COSINE, line_width=23, color='black',
                                   fill_color=None,
                                   legend_label='Random cos() values', size=15)

main_plot.legend.location = "bottom_right"
main_plot.legend.title = 'Random sin & cos functions (using DataSource)'
main_plot.legend.title_text_font_style = "bold"
main_plot.legend.title_text_font_size = "10px"


def handler_sine_plot(event):
    seed_int = random()
    DATA_SOURCE_SINE.data['y_sin'] = [math.sin(i + seed_int) for i in range(10)]


def handler_cosine_plot(event):
    seed_int = random()
    DATA_SOURCE_COSINE.data['y_cos'] = [math.cos(i + seed_int) for i in range(10)]


# add a button widget for the sine functions and set the handler to be called on click
sine_button = Button(label="Click Here to change the Y-Axis DataSource for Sine plot")
sine_button.on_click(handler_sine_plot)

# add a button widget for the cosine functions and set the handler to be called on click
cosine_button = Button(label="Click Here to change the Y-Axis DataSource for Cosine plot")
cosine_button.on_click(handler_cosine_plot)

# configure the root elements in the Document object
curdoc().add_root(column(sine_button, cosine_button, main_plot))

# run the following command from terminal
# bokeh serve e_bokeh_two_lines_data_source.py --show
