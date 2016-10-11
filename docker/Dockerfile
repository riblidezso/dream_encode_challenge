# Build as jupyter/systemuser
# Run with the DockerSpawner in JupyterHub

#FROM jupyter/singleuser
FROM continuumio/anaconda

MAINTAINER ENCODE-ELTE-NODE

USER root
ENV SHELL /bin/bash

#########################################
#baseline dependecies
#########################################
#pybedtools pybigwig
RUN conda install -y -c bioconda pybedtools pybigwig
RUN conda install -y psycopg2=2.6.2 biopython shapely
RUN apt-get update && apt-get install -y bedtools gcc

#pydnabinding
RUN git clone https://github.com/nboley/pyDNAbinding.git
RUN cd pyDNAbinding; python setup.py build; python setup.py install
#install failed to copy this directory
RUN cp -r /pyDNAbinding/pyDNAbinding/shape_data/ /opt/conda/lib/python2.7/site-packages/pyDNAbinding-0.1.1-py2.7-linux-x86_64.egg/pyDNAbinding/

#########################################
# other dependecies
#########################################
RUN apt-get install -y sudo screen
#samtools...
#conda R
#RUN conda install -c https://conda.anaconda.org/r r-essentials

#########################################
# jupyterhub dependecies
#########################################
# Install JupyterHub to get the jupyterhub-singleuser startup script
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install jupyterhub jupyter notebook

#add python2 kernel to jupyter
RUN python -m ipykernel install

#test
#RUN USER_ID=65000 USER=systemusertest sh /srv/singleuser/systemuser.sh -h && userdel systemusertest

#stuff for serving
EXPOSE 8888
ADD systemuser.sh /srv/singleuser/systemuser.sh
CMD ["sh", "/srv/singleuser/systemuser.sh"]
