#!/bin/bash

# Description: Script for the read trimming.

# conda install bioconda::trimmomatic
# https://trimmomatic.com/

eval "$(conda shell.bash hook)"
conda activate qc

PATHTO_TRIMJAR=~/miniconda3/envs/qc/share/trimmomatic-0.40-0/trimmomatic.jar
# ADAPTORPATH=~/home/jan/miniconda3/envs/qc/share/trimmomatic/adapters
# ADAPTER="TruSeq3-PE.fa"

DATA_DIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
HEADCROP="$2" # e.g. 14; positional argument
THREADS="$3" # e.g. 8; positional argument

READ_DIR="$DATA_DIR/raw_reads" # e.g. /home/reads_mg/1; positional argument
OUTDIR_TRIMMOMATIC="$DATA_DIR/trimmomatic_results"


# loop over all files in that directory and its subdirectories
# for READ1 in $READ_DIR/**/*_1.fq.gz; do
for READ1 in $READ_DIR/N*/*_1.fq.gz; do


    READ2=$(echo $READ1 | sed "s/_1.fq.gz/_2.fq.gz/")
    OUTDIR_PE=$OUTDIR_TRIMMOMATIC/PE/$(echo $(basename $(dirname "$READ1")))
    OUTDIR_SE=$OUTDIR_TRIMMOMATIC/SE/$(echo $(basename $(dirname "$READ1")))

    mkdir -p $OUTDIR_PE
    mkdir -p $OUTDIR_SE
    
    echo "processing $READ1 and $READ2" 

    start_time=$(date +%s)

    java -jar $PATHTO_TRIMJAR PE \
        "$READ1" "$READ2" \
        ${OUTDIR_PE}/$(basename $READ1) \
        ${OUTDIR_SE}/$(basename $READ1) \
        ${OUTDIR_PE}/$(basename $READ2) \
        ${OUTDIR_SE}/$(basename $READ2) \
        ILLUMINACLIP:TruSeq3-PE.fa:2:30:10:2:True \
        MINLEN:100 HEADCROP:$HEADCROP\
        SLIDINGWINDOW:4:25 -threads $THREADS \
        

    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "Duration $elapsed_time seconds"
done


# look into seqs
# zcat sample.fastq.gz | head -n 40

# # # unpack results
# # for TRIM in $OUTDIR/**/*.gz; do
# #     gunzip "$TRIM"
# # done
