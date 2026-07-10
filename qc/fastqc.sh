#!/bin/bash

# Description: Script for the initial read QC.

# conda install bioconda::fastqc
# https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

eval "$(conda shell.bash hook)"
conda activate qc

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
DATA_DIR="$2" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$3" # e.g. 8; positional argument

OUT_DIR=$BASEDIR/04_qc/fastqc_results_MTX
# OUT_DIR=$READ_DIR/04_qc/fastqc_results_MGX

READ_DIR="$DATA_DIR/raw_reads" # e.g. /home/reads_mg/1; positional argument

# loop over all files in that directory and its subdirectories
for READ in $READ_DIR/**/*.fastq; do
    fastqc "${READ}" -o "$OUT_DIR" -t $THREADS
done

for READ in $READ_DIR/**/*.gz; do
    fastqc "${READ}" -o "$OUT_DIR" -t $THREADS
done



