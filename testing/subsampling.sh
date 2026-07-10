#!/bin/bash

# conda install bioconda::bbmap

# https://bbmap.org/
# https://bbmap.org/tools/bbnorm

eval "$(conda shell.bash hook)"
conda activate bbmap

BASEDIR=/home/jan/ms/1_mg
BBSCRIPTS=/home/jan/miniconda3/envs/bbmap/bin

SEQ_DIR=$BASEDIR/04_qc/trimmomatic_results/PE
OUTDIR=$BASEDIR/04_qc/trimmomatic_results_subsampled/PE

SAMPLERATE=0.1

mkdir -p $OUTDIR

# loop over all files in that directory and its subdirectories
for READ1 in $SEQ_DIR/**/*_1.fq.gz; do

    READ2=$(echo $READ1 | sed "s/_1.fq.gz/_2.fq.gz/")
    READ_NAME=$(echo $(basename $(dirname "$READ1")))
    
    start_time=$(date +%s)

    # echo $READ1
    # echo $(basename $READ1 .fq.gz)
    # echo $READ2
    # echo $(basename $READ2 .fq.gz)

    $BBSCRIPTS/reformat.sh \
        in=$READ1 \
        in2=$READ2 \
        out=${OUTDIR}/${READ_NAME}/${READ_NAME}_SR${SAMPLERATE}_1.fq.gz \
        out2=${OUTDIR}/${READ_NAME}/${READ_NAME}_SR${SAMPLERATE}_2.fq.gz \
        samplerate=$SAMPLERATE sampleseed=42

    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "Duration $elapsed_time seconds" $(basename $READ1 .fq.gz)

done


