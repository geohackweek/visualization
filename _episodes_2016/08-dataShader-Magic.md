---
title: "title"
teaching: 20
exercises: 0
questions:
- "When traditional GIS tools break down due to data volume, what options do I have to visualize data?" 
objectives:
- "Visualize and interact with large amounts of data at the speed of thought."  
keypoints:
- "DataShader is one of new python based tools that allow you to develop a data processing pipline, while visualizing data in real time."  
---

## Import data 

```python
# CSV is much quicker in this case than geojson
df = pd.read_csv('Zone10_2014_07.csv')
```

## Re-project

You can use dataShader and Bokeh with any type of point data you want. It does not need to be geographically aware. But to put it in context, it is helpful to plot it on a basemap. In our case - the basemap needs point data in a web mercator projection. 

```python
## Datashader needs the location in web mercator coordiates

# WGS 84
inProj = Proj(init='epsg:4326')

# Web mercator 
outProj = Proj(init='epsg:3857')

df['xWeb'],df['yWeb'] = transform(inProj,outProj,df['X'].values,df['Y'].values)
```

We use pyproj and Pandas to transform the coordinate data. 

## Working with time slices

The direct import of the csv to pandas does not handle the data information correctly, so I correct it here. You can also slice the data to within a smaller date and time window if you like.

```python

# set baseDateTime to a proper pandas datetime
df['BaseDateTime'] = pd.to_datetime(df['BaseDateTime'])

# select a slice of data you want to visualize

df_slice = df[(df['BaseDateTime'] > '2014-07-01') & (df['BaseDateTime'] < '2014-07-30')]

```

## now the meaty part 

```python
WA = x_range, y_range = ((df_slice.xWeb.min(),df_slice.xWeb.max()), (4898057.594904038,5565974.539663678))

plot_width  = int(600)
plot_height = int(plot_width//1.2)

def base_plot(tools='pan,wheel_zoom,reset',plot_width=plot_width, plot_height=plot_height, **plot_args):
    p = figure(tools=tools, plot_width=plot_width, plot_height=plot_height,
        x_range=x_range, y_range=y_range, outline_line_color=None,
        min_border=0, min_border_left=0, min_border_right=0,
        min_border_top=0, min_border_bottom=0, **plot_args)

    p.axis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    return p
    
options = dict(line_color=None, fill_color='blue', size=5)

background = "black"
export = partial(export_image, export_path="export", background=background)
cm = partial(colormap_select, reverse=(background=="black"))

def create_image(x_range, y_range, w=plot_width, h=plot_height):
    cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
    agg = cvs.points(df_slice, 'xWeb', 'yWeb',ds.mean('SOG'))
    
    img = tf.shade(agg, cmap=['lightblue','red'], how='eq_hist')
    
    #img = tf.shade(agg, cmap=Hot, how='eq_hist')
    return tf.dynspread(img, threshold=0.5, max_px=4)

p = base_plot()
p.add_tile(STAMEN_TERRAIN)
```

## And finally the magic 

```python
# this export step is not neccesary - it saves a PNG of the file
export(create_image(*WA),"WA_red")

# this is where the magic happens
InteractiveImage(p, create_image)
```

This is a little hard to convey in a blog post without a interactive notebook, but I hope the gif shows a little of the potential. As this tutorial progresses I will put up an interactive version of the iPython notebook.

![Example of Datashading]({{ site.baseurl }}/images/out.gif "dataShading Magic")


