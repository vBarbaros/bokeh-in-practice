from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import Button, FixedTicker

X_AXIS = Y_AXIS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

main_plot = figure(title='Randomly generated line ("bokeh-in-practice", November 2021)',
                   tools="box_select,box_zoom,lasso_select,reset",
                   width=900, height=900)

main_plot.xaxis.axis_label = "Integers (1 through 10)"
main_plot.xaxis.axis_label_text_color = "#aa6666"
main_plot.xaxis.axis_label_standoff = 20
main_plot.xaxis.bounds = (1, 10)
main_plot.xaxis.ticker = FixedTicker(ticks=X_AXIS)

main_plot.yaxis.axis_label = "Randomly generated values (integers)"
main_plot.yaxis.axis_label_text_font_style = "italic"


main_line = main_plot.line(x=X_AXIS, y=Y_AXIS, line_width=2, color='red', legend_label='Random integers')
main_circle = main_plot.circle(x=X_AXIS, y=Y_AXIS, line_width=2, color='red', legend_label='Random integers', size=10)

data_source_line = main_line.data_source
data_source_circle = main_circle.data_source


def handler_main_plot(event):
    new_data = dict()
    new_data['x'] = X_AXIS
    new_data['y'] = [random() for i in range(10)]
    data_source_line.data = new_data
    data_source_circle.data = new_data


# add a button widget and set the handler to be called on click
main_button = Button(label="Click Here")
main_button.on_click(handler_main_plot)

# configure the root elements in the Document object
curdoc().add_root(column(main_plot, main_button))

# run the following command from terminal
# bokeh serve bokeh_simple_line.py --show
