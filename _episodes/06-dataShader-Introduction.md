---
title: "Introduction to dataShader"
teaching: 20
exercises: 0
questions:
- When traditional GIS tools break down due to data volume, what options do I have to visualize data? 
objectives:
- Visualize and interact with large amounts of data at the speed of thought.  
keypoints:
- DataShader is one of new python based tools that allow you to develop a data processing pipline, while visualizing data in real time.  
---

## Motivation 

I am stubborn when it comes to geographic data. I believe that data should be visualized and analysed at the scale it is collected at. However, often the data overwhelms the processing capabilities of scientists. At other times, it doesn't need to be analysed at that extreme scale. 

That said, with a wealth earth observing satellites, envirnmental sensors, and tools such as [LiDAR](https://en.wikipedia.org/wiki/Lidar), scientists often have more data than they know what to do with. Outside of academia, location data can be even more massive, such cell phone location data. This stubborness is why I get excited when I come across tools that let me interact with data at the scale it was actually collected at- tools like [dataShader](https://github.com/bokeh/datashader).To explore this type of data, I am using [marine AIS vessel location data](http://marinecadastre.gov/ais/), from the U.S. Coast Guard. 

I came across it when I was exploring a very basic question - where should I go kayaking if I don't want to get run over or massively waked out by marine traffic in Puget Sound? This data is perhaps not truely 'big', but one month takes up about 800 mb when zipped, and it takes arcGIS a long time to load (which might be a working definition of big data for [GIS](https://en.wikipedia.org/wiki/Geographic_information_system)  folks.) It  represents about 23 million point locations.   

## Preliminary Steps - Convert data into a better format
The data was donwloaed from [marinecadastre.gov](http://marinecadastre.gov/ais/). It is formatted as .gdb. Step one is to convert it to something more flexible. To do so, I use the built in tools QGIS has take a .gdb and save it both a .csv and and .geoJson. These files are big, but they are a start.

| data type     | size (GB)     | 
| ------------- |:-------------:| 
| ucompressed GDB      | 2.65 | 
| CSV     | 2.35      | 
| geoJSON |7.95      |


