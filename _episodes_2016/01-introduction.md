---
title: "Introduction to visualization"
teaching: 15
exercises: 0
questions:
- "What are some common methods for visualizing geospatial data?"
- "What different approaches are needed for vector versus raster data?"
- "When would I need static versus dynamic maps?"
- "What tools can I use when traditional visualization (such as GIS software) tools won't work?"
objectives:
- gain an overview of different types of visualization technologies
keypoints:
- "decision often centered around should I use a GUI or script?"
---
### Overview:
Visualizing information is one of the most powerful ways to understand data. Humans, it has been said, are visual creatures. Yet the tools employed by geospatial science often have not kept up with the pace of data aquisition. However, new tools have emerged that help cope with this torrent of data. We will cover are range of visualization tools - from basics such as using matplotlib, to more advanced approaches such as [CesiumPy](https://pypi.python.org/pypi/cesiumpy). 

### Beyond GIS software:

We are assuming that most participants have expereince with Geographic Information Systems. Because of this, we are not teaching GIS software in this course.  This is not unversally true - for example, some instructors have worked directly with python tools without needing GIS. Because of this assumption of GIS experience, if we mention terms that are not familiar - please let us know. 

This tutorial is going to present visualizing geospatial data in three tiers. 

1. Basic Python Visualization tools
  - [Matplotlib](http://matplotlib.org/)

2. Intermediate tools
  - displaying multiple datasets
  - handling projections

3. Cutting Edge Tools
  - time dynamic data 
  - Cesium 
  - dataShader

### Worldwide Telescope

This PC-only application can be downloaded [here](http://worldwidetelescope.org "WWT main site"). It uses your computer's GPU to do two things: Render the earth in high resolution (as good as 2 meters) with topography; and render data structures with as many as six dimensions in that geospatial context. 

The benefits of using Worldwide Telescope and the drawbacks are outlined below. For a faster video intro to what is possible
using this remarkable (free) application we suggest YouTube, particularly [this video](https://youtu.be/JLu6caZmbRg "Excel Add In for WWT"). An extended tutorial is [here](https://youtu.be/Nkardcd5vo0 "WWT extended tutorial for earth science"). Contact Rob Fatland at the University of Washington for a conversational perspective.

#### Advantages
* Easy exchange of tabular data: CSV files, Excel spreadsheets, WWT
* Time control: Enables rendering time-series geospatial data
* Control brightness, color, marker style, time persistence of point-like data
* Control opacity, color, location, time persistence of vector data
* Overlay (drape) raster imagery over terrain
* Almost-completely-free control of perspective
* Time looping
* Can build narrative stories called Tours
* Application includes views beyond earth: Various planets including Mars and the Moon, solar system, galaxy, universe, ...
* WWT features an API for data exchange
* Layer Manager enables you to control what you are looking at and how you look at it

#### Disadvantages
* Basics require time to master (hours) 
* Advanced features require a considerable investment of time (days to weeks to months)
* Requires you to operate a PC or install a PC emulator
* WWT has idiosyncracies that can try your patience; it is sort of the Mazerati of free geospatial visualization apps.
