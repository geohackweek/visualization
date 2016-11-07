FROM continuumio/anaconda
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y gfortran
RUN conda install basemap
RUN conda install -c conda-forge ipyleaflet
RUN conda install lxml
RUN pip install cesiumpy
RUN pip install pykml
RUN mkdir src/
COPY /src/ /src
RUN python /src/clawpack-5.3.1/setup.py install
RUN echo 'export CLAW=/src/clawpack-5.3.1' >> ~/.bashrc
RUN echo 'export FC=gfortran' >> ~/.bashrc
RUN pip install -e git+https://github.com/jakevdp/JSAnimation.git#egg=JSAnimation 
RUN mkdir /notebooks
COPY /notebooks/ /notebooks
RUN mkdir /geoclaw_output
COPY /geoclaw_output/ /geoclaw_output
