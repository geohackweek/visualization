FROM continuumio/anaconda
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN conda install basemap
RUN conda install -c conda-forge ipyleaflet
RUN conda install lxml
RUN conda install bokeh
RUN conda install -c bokeh datashader
RUN pip install cesiumpy
RUN pip install pykml
RUN pip install pyproj
RUN pip install -e git+https://github.com/jakevdp/JSAnimation.git#egg=JSAnimation 
RUN mkdir /notebooks
COPY /notebooks/ /notebooks
RUN mkdir /geoclaw_output
COPY /geoclaw_output/ /geoclaw_output
RUN mkdir /data
COPY /data/ /data
