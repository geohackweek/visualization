---
title: "Basics: Quick + Simple maps with <code>cartopy</code>."
teaching: 20
excercises: 0
questions:
- "What is <code>cartopy</code>? How can it help with visualization?"
- "How do I create a simple map in Python?"
objectives: 
- Set up a basemap using <code>cartopy</code>
- Change projections on basemap.
- Understand interface between standard <code>matplotlib</code> plotting and <code>cartopy</code>.
---

>## Notebook
>This tutorial is accompanied by a Jupyter notebook, which can be found [here](#). **TODO: put link**
{: .prereq}


>## Why Cartopy?
>The Python package ecosystem is robust, which means that usually there are several packages which all attempt to satisfy the same need. The landscape of mapping packages is no different. We've chosen cartopy for two reasons: 1) the authors of this tutorial and our scientific communities have made extensive use of cartopy and have found that it does its job well and comprehensively, and 2) it's engineered for scientists and maintained by an active development community. 
{: .callout}

## Cartopy 101
For our purposes here, cartopy is a python package which provides a set of tools for creating projection-aware geospatial plots using python's standard plotting package, `matplotlib`. Cartopy also has a robust set of tools for defining projections and reprojecting data, which are used under-the-hood in our tutorial, but won't be covered in depth here. 

The bottom line is that Cartopy provides a very easy, cartographically accurate method for producing maps, and pairs well with other Python tools like `geopandas`. 

## Building Blocks
Cartopy has several fundamentals which are useful to conceptualize, outlined below. 

### 1) Projections ([`cartopy.crs`](#))
A central utility of the cartopy package is the ability to define, and transform data among, cartographic projections. The `cartopy.crs` module (CRS = coordinate reference system a.k.a. projection) defines a set of projections which are useful in defining the desired projection of a plot. These projections augment the machinery of `matplotlib` to allow for geospatial plots.

### 2) Features ([`cartopy.feature`](#))
Cartopy also contains a module for accessing geospatial data files, like shapefiles or GeoJSON. It has a convenient set of data loaders for adding context to maps (like coastlines, borders, place names, etc.). We'll use this module in the example below. 

## Making a Map
Typically, when creating a new plot in `matplotlib`, we employ a set of commands like so: 

    ax = plt.axes()           # create a set of axes
    ax.scatter(x, y, ax=ax)   # plot some data on them
    ax.set_title("Title")     # label it
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    plt.show()

This creates a plot somewhat akin to this: 
<table align='center'>
    <tr align='center' style="width: 100%">
        <td>
            <img src="{{site.root}}/assets/img/test-plot.png" style="width: 100%"/>
        </td>
    </tr>
</table>

Spatial data is unique because plots containing it (i.e., maps) have *specialized axes*. Think about it: looking at your favorite projection, the gridlines *aren't necessarily straight*, nor are they evenly-spaced, like they would be if we drew lines onto the plot above. 

For this reason, we employ cartopy to define the mapping between our data and our visualization. Here's how: the `plt.axes()` function takes a `projection = ` argument. Knowing this, we only need to change two lines of our above code as follows:

    import cartopy.crs as ccrs                   # import projections
    import cartopy.feature as cf                 # import features
    ax = plt.axes(projection = ccrs.Mercator())  # create a set of axes with Mercator projection
    ax.add_feature(cf.COASTLINE)                 # plot some data on them
    ax.set_title("Title")                        # label it
    plt.show()

This creates a plot as follows; 

<table align='center'>
    <tr align='center' style="width: 100%">
        <td>
            <img src="{{site.root}}/assets/img/test-geo.png" style="width: 100%"/>
        </td>
    </tr>
</table>

Simple! To change the projection of the data, all we need to do is modify that first line. 
           
    ax = plt.axes(projection = ccrs.LambertConformal())  
    ax.add_feature(cf.COASTLINE)                 
    ax.set_title("Title")                        
    plt.show()


<table align='center'>
    <tr align='center' style="width: 100%">
        <td>
            <img src="{{site.root}}/assets/img/test-lambert.png" style="width: 100%"/>
        </td>
    </tr>
</table>
