---
title: "Basics: Projections"
teaching: 20
exercises: 0
questions:
- How do map projections work? How can Python help me manage them?
objectives:
- The Earth is Round
- There are lots of ways to make it flat.
keypoints:
- Map projections are interesting, complicated, and mostly handled for us.
- Choosing a projection appropriately to match the intent of the visualization is critical to accurately conveying information ("how much distortion is OK?").
---



##  The Earth is Round
<table align='center'>
    <tr align='center' style="width: 100%">
        <td>
            <img src="{{site.root}}/assets/img/orange.png" style="width: 100%"/>
        </td>
    </tr>
    <tr align='center'>
        <td>Flattened Orange (e.g. <a href='https://en.wikipedia.org/wiki/Goode_homolosine_projection'>Goode Homolosine</a> projection)</td>
    </tr>
</table>

The Earth is round (ok, ellipsoidal), paper and computer screens are flat. This means that when we attempt to flatten our round planet to the two-dimensional plane of websites and journal articles, we make **certain assumptions** based on the intent we've set for our map. 

For example: perhaps being able to compare area across the globe is critical (i.e. a two-cm square anywhere on our paper map has the same surface area on the globe), or perhaps preserving the 'real' shapes of landmasses is important. **Each set of assumptions and tradeoffs we create is referred to as a "projection,"** and consists of a set of equations which convert spherical (or, in the case of Earth, ellipsoidal) coordinates into planar coordinates.

Those "spherical coordinates" I mention above are referencing a location on a sphere (or, in the case of Earth, an elipse), and as such they have to be in reference to some definition of that sphere. We call that reference point a datum, which defines the surface upon which the unprojected spherical coordinates lie. There are several important datums, like WGS84 (used by GPS systems) and NAD83, which you'll see often. They each define a different version of the Earth's geometry, and that's all we'll say about that here (it's easy to get into a rabbit hole with datums/geographic reference systems, so we'll avoid that). For more on this, start at [this discussion](https://gis.stackexchange.com/questions/664/whats-the-difference-between-a-projection-and-a-datum) (thanks Randy for the reference!).

Each of these projections has been assigned a code by the European Petroleum Survey Group (EPSG), which has established itself as a projection authority. This has made using specific projections quite simple, as one can refer to them by their EPSG code. The EPSG code for the Web Mercator projection (used by Google Maps and Bing Maps), for example, is `EPSG:3857`. You can explore projections and find your neighborhood's favorite at [http://epsg.io](http://epsg.io).

Some Examples ([comic](https://xkcd.com/977/)):
<table align="center">
    <tr align="center">
        <td><img style="width: 100%" src="https://i.guim.co.uk/img/static/Guardian/global/gallery/2009/apr/17/geography/mercator-5130.jpg?w=1010&q=20&auto=format&usm=12&fit=max&dpr=2&s=7fee64700cc5a92d3ffd1ad6306ad53e"/>
        </td>
        <td><img style="width: 100%" src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Lambert_conformal_conic_projection_SW.jpg/700px-Lambert_conformal_conic_projection_SW.jpg'/></td>
        <td>
            <img style="width: 100%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Winkel_triple_projection_SW.jpg/700px-Winkel_triple_projection_SW.jpg"/>
        </td>   
    </tr>
    <tr align="center" style="height: 20px">
        <td>Mercator (web maps)</td>
        <td>Lambert Conformal Conic (weather maps)</td>
        <td>Winkel-Tripel (National Geographic maps)</td>
    </tr>
</table>
See [here](https://bl.ocks.org/syntagmatic/ba569633d51ebec6ec6e) for a nice visualization of different projections by github user [`syntagmatic`](https://github.com/syntagmatic). 


>## EPSG Codes 
> Each of these projections has been assigned a code by the European Petroleum Survey Group (EPSG), which has established itself as a projection authority. This has made using specific projections quite simple, as one can refer to them by their EPSG code. The EPSG code for the Web Mercator projection (used by Google Maps and Bing Maps), for example, is EPSG:3857. You can explore projections and find your neighborhood's favorite at http://epsg.io, which is also the database cartopy uses to lookup projections by their EPSG codes.
{: .callout}

## This Sounds Complicated!

It is. Fortunately, much of the work to manage these map projections, at least in Python, has been done for us. In the next episode in this tutorial we'll use [`cartopy`](https://scitools.org.uk/cartopy/docs/latest/) to help turn a standard Python plotting tool into a powerful, projection-aware mapping utility. 

