---
title: "Old vs. New Way"
teaching: 15
exercises: 0
questions:
- 
objectives:
- 
keypoints:
- 
---

## The old way
![an image alt text]({{ site.baseurl }}/images/Screen Shot 2016-07-27 at 3.30.16 PM.png "The old way")

As I said at the start, the standard way to handle this data is to plot your program in a [geographic information system] (https://en.wikipedia.org/wiki/Geographic_information_system) such as arcGIS. This route is painful and makes the data very hard to quickly explore. Each data point is individually drawn. If you move the area of interest even a little bit, ArcGIS trys to re-draw everything again. QGIS is a little better (it draws the points much more quickly - but suffers from the same issues. Enter Bokeh and DataShader. 

## The new way 

First, you need to install bokeh and datashader, then import them

```python
import pandas as pd
import numpy as np
```

Pyproj is used to reproject the data later.

```python
from pyproj import Proj, transform
```

```python
import datashader as ds
from datashader import transfer_functions as tf
from datashader.bokeh_ext import InteractiveImage
from datashader.utils import export_image
from datashader.colors import colormap_select, Greys9, Hot, viridis, inferno

from IPython.core.display import HTML, display

from bokeh.plotting import figure, output_notebook, output_file, show
```

[Stamen Maps](http://maps.stamen.com/) offers up beautiful map tiles that can be accessed by Bokeh. 

```python 
from bokeh.tile_providers import STAMEN_TERRAIN
from bokeh.tile_providers import STAMEN_TONER
from bokeh.embed import file_html

from functools import partial

output_notebook()
```
