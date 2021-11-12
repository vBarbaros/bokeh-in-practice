import math
from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, FixedTicker

X_AXIS = Y_AXIS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

main_plot = figure(
    title='Two separate lines, cos & sin, with randomly generated values ("bokeh-in-practice", November 2021)',
    tools="box_select,box_zoom,lasso_select,reset",
    width=900, height=900)

main_plot.xaxis.axis_label = "Integers (0 through 9)"
main_plot.xaxis.axis_label_text_color = "#aa6666"
main_plot.xaxis.axis_label_standoff = 20
main_plot.xaxis.bounds = (-1, 10)
main_plot.xaxis.ticker = FixedTicker(ticks=X_AXIS)

main_plot.yaxis.axis_label = "Randomly generated (sin vs cos) values"
main_plot.yaxis.axis_label_text_font_style = "italic"

main_line_sin = main_plot.line(x=X_AXIS, y=Y_AXIS, line_width=2, color='red', line_dash=[2, 2],
                               legend_label='Random sin() values')
main_circle_sin = main_plot.circle(x=X_AXIS, y=Y_AXIS, line_width=2, color='blue', legend_label='Random sin() values',
                                   size=10)

main_line_cos = main_plot.line(x=X_AXIS, y=Y_AXIS, line_width=2, color='green', line_dash=[4, 4],
                               legend_label='Random cos() values')
main_square_cos = main_plot.square(x=X_AXIS, y=Y_AXIS, line_width=2, color='black', fill_color=None,
                                   legend_label='Random cos() values', size=10)

main_plot.legend.location = "bottom_left"
main_plot.legend.title = 'Random sin & cos functions'
main_plot.legend.title_text_font_style = "bold"
main_plot.legend.title_text_font_size = "10px"

data_source_line_sin = main_line_sin.data_source
data_source_circle_sin = main_circle_sin.data_source

data_source_line_cos = main_line_cos.data_source
data_source_square_cos = main_square_cos.data_source


def handler_sine_plot(event):
    seed_int = random()
    new_data_sine = dict()
    new_data_sine['x'] = X_AXIS
    new_data_sine['y'] = [math.sin(i + seed_int) for i in range(10)]
    data_source_line_sin.data = new_data_sine
    data_source_circle_sin.data = new_data_sine


def handler_cosine_plot(event):
    seed_int = random()
    new_data_cos = dict()
    new_data_cos['x'] = X_AXIS
    new_data_cos['y'] = [math.cos(i + seed_int) for i in range(0, 10)]
    data_source_line_cos.data = new_data_cos
    data_source_square_cos.data = new_data_cos


# add a button widget for the sine functions and set the handler to be called on click
sine_button = Button(label="Click Here to change Sine plot")
sine_button.on_click(handler_sine_plot)

# add a button widget for the cosine functions and set the handler to be called on click
cosine_button = Button(label="Click Here to change Cosine plot")
cosine_button.on_click(handler_cosine_plot)


# configure the root elements in the Document object
curdoc().add_root(column(main_plot, sine_button, cosine_button))

# run the following command from terminal
# bokeh serve d_bokeh_two_lines_separate_handler.py --show
