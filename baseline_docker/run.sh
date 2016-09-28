#!/bin/bash

tf=$1

input_path=/mnt/vdisk/data/synapse/encodeChallenge_Data/
baseline_path=~/baseline/

sudo docker run -it -v $input_path:/encodeChallenge_Data/ \
-v $baseline_path:/root/baseline \
riblidezso/encode_challenge_baseline_docker  $tf

