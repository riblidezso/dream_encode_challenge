import pandas as pd
DATA_DIR='/mnt/vdisk/data/synapse/'
ALL_TF=['ATF2','CTCF','E2F1','EGR1','FOXA1','FOXA2','GABPA','HNF4A','JUND','MAX','NANOG','REST','TAF1']

def load_labels(t_factor,label_dir):
    """Load the labels for a transcription factor for all cell lines."""
    labels_fname = label_dir + t_factor + ".train.labels.tsv.gz"
    #load the original
    temp_df=pd.read_table(labels_fname,header=0,index_col=(0,1,2))
    #change U,A,B to U,A->0 B->1!!
    temp_df[(temp_df=='U') | (temp_df=='A')]=0
    temp_df[temp_df=='B']=1
    return temp_df


#load a fold coverage table to be used for merging
fc=pd.read_hdf(DATA_DIR+'fold_cov_data/A549_dnase_fold_cov.hdf',
                     'dnase_fold_cov',index_col=(0,1,2))

for tf in ALL_TF:
    print tf,
    
    #load labels
    labels=load_labels(tf,DATA_DIR+'/labels/')
    
    # fill in the chromosome positions missing from the label with 0-s
    labels=pd.concat([labels,fc],axis=1,join='outer')[labels.columns]
    labels.fillna(0,inplace=True)
    
    labels.to_hdf('extended_labels/'+tf+'_labels.hdf','labels')
