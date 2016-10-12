# Dream encode challenge



## final_sub_09_30 folder

This folder contains the notebooks which create the submissions for every TF-CELL line pair for the final submission. Its read the data tables created by me (described below), models with SGD logistic regression, uses a validation cell line if possible, and creates the submission.

Note: Here I have used TF binding labels from the training cell lines as inputs, but this should not be used like this in the future. The positions which will be evaluated are on chromosomes without this kind of data. (Here I put 0-s as inputs to those chromosomes.)

## lb_subs_09_30 folder

It contains notebook about the 1 and only leaderboard submission we have made so far. It does not use the labels from other cell lines as inputs. It validates the results using a local validation cell line and local validation chromosomes. The local validation result was very close the results on the leaderboard, therefore I think we can use this validation scheme for further experiments.

## create_data_tables folder

I made 3 scripts to create input tables from the raw data. The tables are saved on the dblab machine on (/mnt/vdisk/data/synapse/tables). This folder is mounted in the jupyterhub as a readonly volume in /tables . The files are pandas dataframes saved in hdf format. They can be read fast (~10s per file).

### Motif data

There is a file for every transcription factor in the format TFNAME_motif.hdf . These files were created with the create_motif_data.py script. They contain the chromosome positions as index e.g.: (chr1,600,800), and some aggregate values which describe the presence of a motif associated with the transciption factor at that genomic region (quantile values). The files can be read using pandas in python:

```
import pandas as pd
ctcf_motif_df=pd.read_hdf("/tables/motif/CTCF_motif.hdf","motif")
```

### Fold coverage data

There is a file for every cell line in the format CellLineName_dnase_fold_cov.hdf. These files were created with the create_fold_cov_data.py script. They contain the chromosome positions as index e.g.: (chr1,600,800), and the number of reads mapping to the region in the DNASE ChipSeq experiment. This value indicated the accesibility of the DNA at the region, the higher the coverage the more accessible the region is. The files

```
import pandas as pd
A549_fc_df=pd.read_hdf("/tables/dnase_fc/A549_dnase_fold_cov.hdf","dnase_fold_cov")
```

### Extended labels

The labels were not given in this challenge for the chromosomes which will be evaluated (chr1,chr8,ch21). To make matching inputs and output fast and convenient I have joined the index of the input tables with the label tables, and filled in the labels on the missing chromosomes with NA-s. Using these extended label tables the order of entries in the input tables and the label tables is the same.
These files were created with the create_extended_labels.py script and they can be opened in the following way:

```
import pandas as pd
A549_labels_df=pd.read_hdf("/tables/labels/ATF2_labels.hdf","labels")
```
## my_baseline notebook

#### Dissected and reproduced the baseline script

- I cut the originial loader class (which takes around 6-8 hours for me to run) into separate loader functions for the different columns of the input.
- I have done some small and easy parallelization (3-10x faster).
- Some parts are not complete, and has to be understood in the baseline.


## Docker

Dockefile for the docker image our jupyter hub is running.
