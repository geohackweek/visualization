---
title: "Interactive Maps"
teaching: 15
exercises: 0
questions: 
    - "How do I create a map I can interact with using Python?"
    - "What packages are available for this?"
objectives:
    - "Use <code>folium</code> to create a simple slippy map with <code>geopandas</code> data."
    - "See other packages in use for this purpose."
---

## Interactive Maps

Static maps, like the sort you'd develop for a publication or brochure, are worthwhile for their durability, flexibility, and relative ease in creation. However, in a time where the creation of public-facing research products is demanded by an increasing range of domains (& funding sources), being able to create interactive, web-based displays of geospatial data is critical.

There are myriad ways to approach this challenge. Hard-core web developers can roll their own websites from scratch in Javascript, HTML, and CSS, leveraging their own data APIs and maintaining their own cyberinfrastructure. Hard-core domain researchers can simply put some easy-to-read plots on a simple website and call it a day. Somewhere in between lies the ability to take an already-polished data analysis pipeline in Python and output the geospatial results to a web-friendly map ready to be hosted on a simple static hosting solution (like your departmental web server or Amazon S3).

That's the intent of the Python package [folium](https://github.com/python-visualization/folium): to combine data objects in Python with a web mapping framework known as Leaflet to produce interactive geospatial data products on the web.

**Note**: at this point, there are several packages which claim to accomplish what Folium does. Packages like [`mapbox-gl-jupyter`](https://github.com/mapbox/mapboxgl-jupyter) and [`Holoviews/Geoviews`](http://geoviews.org/) can accomplish much of Folium's core functionality, but have strengths and weaknesses of their own. Folium is a great way to learn these frameworks, but if you have a specific plotting need, know that there are several very powerful options out there which may better suit your needs. 

This tutorial lives in its entirety [here](https://github.com/geohackweek/tutorial_contents/tree/master/visualization/notebooks), in a notebook called `foliumTutorial`. 