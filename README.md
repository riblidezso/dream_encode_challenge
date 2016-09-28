# Dream encode challenge

## Baseline docker
I have created a docker image which is able to run the baseline script. 

The image can be pulled from dockerhub ( or can be built from the Dockerfile ).

```docker pull riblidezso/encode_challenge_baseline_docker```

You can run the image with the script i made. It mounts the data, and ~/baseline, runs the baseline, and the results should be in ~/baseline.

```./run.sh [TF_name]```

