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


