#!/bin/bash

# Description: Script for generating and subsampling metagenomic reads before other steps.
# further info & instructions https://insilicoseq.readthedocs.io/en/latest/iss/install.html

eval "$(conda shell.bash hook)"
conda activate omics

BASEDIR=/home/jan/ms/1_mg

MULTIFASTA=$BASEDIR/02_genomes/genomes_multifasta.fasta
OUT_DIR=$BASEDIR/03_reads/raw/
SUBSAMPLED_DIR=$BASEDIR/03_reads/raw_subsampled/
CORE_NR=8 # Set the number of cores

# Task 1: Generate raw reads
for i in {1..4}; do
    mkdir ${OUT_DIR}run_${i}
    iss generate --cpus $CORE_NR --genomes ${MULTIFASTA} --n_reads 2000000 --model novaseq --output ${OUT_DIR}run_${i}/
done
