FROM continuumio/anaconda

RUN conda install -y -c bioconda pybedtools
RUN conda install -y -c bioconda pybigwig

#pydnabinding
RUN apt-get update; apt-get install -y gcc
RUN conda install -y psycopg2=2.6.2
RUN git clone https://github.com/nboley/pyDNAbinding.git
RUN cd pyDNAbinding; python setup.py build; python setup.py install
#install failed to copy this directory
RUN cp -r /pyDNAbinding/pyDNAbinding/shape_data/ /opt/conda/lib/python2.7/site-packages/pyDNAbinding-0.1.1-py2.7-linux-x86_64.egg/pyDNAbinding/

RUN conda install -y shapely
RUN apt-get install -y bedtools

WORKDIR /root/baseline
ENTRYPOINT ["python","baseline.py"]
