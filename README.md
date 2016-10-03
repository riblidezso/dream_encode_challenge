# Dream encode challenge


## my_baseline notebook

#### Dissected and reproduced the baseline script

- I cut the originial loader class (which takes around 6-8 hours for me to run) into separate loader functions for the different columns of the input.
- I have done some small and easy parallelization (3-10x faster).
- Some parts are not complete, and has to be understood in the baseline.

## final_sub_09_30 folder

This folder contain the notebook which create the submissions for every TF-CELL line pair for the final submission. It read the data tables created by me (described below), models with SGD logistic regression, uses a validation cell line if possible, and creates the submission.

## create_data_tables folder

I made 3 scripts to create input tables from the raw data. The tables are saved on the dblab machine on (/mnt/vdisk/data/synapse/motif_data, fold_cov_data,extended_labels ). The files are pandas dataframes saved in hdf format. They can be read fast (~10s per file).

### Motif data

There is a file for every transcription factor in the format TFNAME_motif.hdf . These files were created with the create_motif_data.py script. They contain the chromosome positions as index e.g.: (chr1,600,800), and some aggregate values which describe the presence of a motif associated with the transciption factor at that genomic region (quantile values). The files can be read using pandas in python:

```
import pandas as pd
ctcf_motif_df=pd.read_hdf("/mnt/vdisk/data/synapse/motif_data/CTCF_motif.hdf","motif")
```

### Fold coverage data

There is a file for every cell line in the format CELLLINENAME_dnase_fold_cov.hdf. These files were created with the create_fold_cov_data.py script. They contain the chromosome positions as index e.g.: (chr1,600,800), and the number of reads mapping to the region in the DNASE ChipSeq experiment. This value indicated the accesibility of the DNA at the region, the higher the coverage the more accessible the region is. The files

```
import pandas as pd
A549_fc_df=pd.read_hdf("/mnt/vdisk/data/synapse/fold_cov_data/A549_dnase_fold_cov.hdf","dnase_fold_cov")
```

### Extended labels

For every transciption factor they originally provided a file containing the measurements. But the regions in these files did not exactly match the ones described in test_regions.blacklistfiltered.bed.gz which is the file that had to be used for the submissions. So I made extended label files which contain these regions. The regions not listed in the original data were filled in with 0-s. This is not reasonable, and I have only done it to be able to finish in time. The missing regions are 3 whole chromosomes, and these should be dealt with in a sensible way in the future. These files were created with the create_extended_labels.py script and they can be opened in the following way:

```
import pandas as pd
A549_labels_df=pd.read_hdf("/mnt/vdisk/data/synapse/extended_labels/ATF2_labels.hdf","labels")
```

## Baseline docker
I have created a docker image which is able to run the baseline script. 

The image can be pulled from dockerhub ( or can be built from the Dockerfile ).

```docker pull riblidezso/encode_challenge_baseline_docker```

You can run the image with the script i made. It mounts the data (/mnt/vdisk/data/synapse/encodeChallenge_Data/), and ~/baseline, runs the baseline, and the results should be in ~/baseline.

```./run.sh [TF_name]```
