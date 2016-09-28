# Dream encode challenge

## Baseline docker
I have created a docker image which is able to run the baseline script. 

The image can be pulled from dockerhub ( or can be built from the Dockerfile ).

```docker pull riblidezso/encode_challenge_baseline_docker```

You can run the image with the script i made. It mounts the data (/mnt/vdisk/data/synapse/encodeChallenge_Data/), and ~/baseline, runs the baseline, and the results should be in ~/baseline.

```./run.sh [TF_name]```

## My baseline notebook

#### Dissected and reproduced the baseline script

- I cut the originial loader class (which takes around 6-8 hours for me to run) into separate loader functions for the different columns of the input.
- I have done some small and easy parallelization (3-10x faster).
- Some parts are not complete, and has to be understood in the baseline.

