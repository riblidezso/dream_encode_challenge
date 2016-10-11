# Build as jupyter/systemuser
# Run with the DockerSpawner in JupyterHub

FROM jupyter/singleuser

MAINTAINER ENCODE-ELTE-NODE

USER root
ENV SHELL /bin/bash

#baseline
#pybedtools pybigwig
RUN conda install -y -c bioconda pybedtools pybigwig
RUN conda install -y psycopg2=2.6.2 biopython
RUN apt-get install -y bedtools


#pydnabinding
RUN apt-get update; apt-get install -y gcc
RUN conda install -y psycopg2=2.6.2
RUN git clone https://github.com/nboley/pyDNAbinding.git
RUN cd pyDNAbinding; python setup.py build; python setup.py install
#install failed to copy this directory
RUN cp -r /pyDNAbinding/pyDNAbinding/shape_data/ /opt/conda/lib/python2.7/site-packages/pyDNAbinding-0.1.1-py2.7-linux-x86_64.egg/pyDNAbinding/

RUN conda install -y shapely

#genome
ADD hg19.fa /opt/hg19.genome.fa

#samtools...

#other
#samtools...

#conda R
RUN conda install -c https://conda.anaconda.org/r r-essentials

ADD systemuser.sh /srv/singleuser/systemuser.sh

RUN USER_ID=65000 USER=systemusertest sh /srv/singleuser/systemuser.sh -h && userdel systemusertest

CMD ["sh", "/srv/singleuser/systemuser.sh"]
