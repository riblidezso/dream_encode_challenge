import os, sys,time
from multiprocessing import Pool
from multiprocessing import sharedctypes
from numpy import ctypeslib
from functools import partial

import numpy as np
import pandas as pd

import pyBigWig

from pyDNAbinding.binding_model import DNASequence, PWMBindingModel, DNABindingModels, load_binding_models


def load_dnase_fold_cov(cell_line,
                        n_proc=12,
                        dnase_fold_cov_dir=DNASE_FOLD_COV_DIR ):
    """Load the raw fold coverage for a t factor and cell line."""
    dnase_fold_cov_fname = dnase_fold_cov_dir + 'DNASE.'+cell_line+'.fc.signal.bigwig'
    
    #partially apply the scorer function
    part_get_dnase_fold_cov_from_region=partial(get_dnase_fold_cov_from_region,
                                                fn=dnase_fold_cov_fname)
    #parallel execute it
    Pool(n_proc).map(part_get_dnase_fold_cov_from_region,xrange(len(idx)))

    #return a dataframe
    return pd.DataFrame({cell_line+'_dnase_fc' : fold_cov},index=idx)

def get_dnase_fold_cov_from_region(i,fn=None):
    """Get raw dnase fold coverage for a region."""
    contig,start,stop=idx[i]
    bigwig_f=pyBigWig.open(fn)
    fold_cov[i]=bigwig_f.stats(contig,start,stop)[0]
    bigwig_f.close()
    return



DNASE_FOLD_COV_DIR ="fold_coverage_wiggles/"
ALL_CELL_LINES=[x.split('.')[1] for x in os.listdir(DNASE_FOLD_COV_DIR)]

idx=pd.read_csv(
    'test_regions.blacklistfiltered.bed.gz',
    index_col=(0,1,2),
    sep='\t').index


#global shared result array... is there a better way?
fold_cov = sharedctypes.RawArray('d', len(idx))

for cl in ALL_CELL_LINES:  
    print cl,
    dnase_fc_df=load_dnase_fold_cov(cl)
    dnase_fc_df.to_hdf('fold_cov_data/'+cl+'_dnase_fold_cov.hdf',
                       'dnase_fold_cov')
