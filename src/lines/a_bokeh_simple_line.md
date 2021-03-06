### (a) Simple Line Example
step 1 - import all you need
```
from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import Button
```

step 2 - instantiate the `datasource` (in this simple case, use the same array for both X & Y axis)
```
X_AXIS = Y_AXIS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
```

step 3 - define a `figure` object with minimal size params, only
```
main_plot = figure(width=900, height=900)
```

step 4 - define the main `line` in our figure, again, with minimal params
```
main_line = main_plot.line(x=X_AXIS, y=Y_AXIS, line_width=2, color='red')
```

step 5 - define a variable that references our `data_source` of the defined `main_line`; 
this will give you the possibility to change the `data` interactively, from our dashboard
```
data_source = main_line.data_source
```

step 6 - define a `handler` function that will be called on an event and define our changes
of the `data`, as you wish (I chose to add new entries all the time using some random values times
2021, because it's in the year of 2021 that we started this repository ;) )
```
def handler_main_plot(event):
    new_data = dict()
    new_data['x'] = data_source.data['x'] + [random() * 2021]
    new_data['y'] = data_source.data['y'] + [random() * 2021]
    data_source.data = new_data
```

step 7 - add a `button` widget and set the `handler` to be called on each click
```
button = Button(label="Click Here")
button.on_click(handler_main_plot)
```

step 8 - configure the `root` elements in the `Document` object
```
curdoc().add_root(column(main_plot, button))
```

step 9 - run the following command from terminal
- it should open a browser at `http://localhost:5006/bokeh_simple_line`
```
$ cd src/lines/
$ bokeh serve a_bokeh_simple_line.py --show
```

step 10 - enjoy it!
![bokeh_simple_line.gif](../../images/lines/a_bokeh_simple_line.gif)