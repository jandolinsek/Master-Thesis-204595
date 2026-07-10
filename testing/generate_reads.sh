#!/bin/bash

# Description: Script for generating and subsampling metagenomic reads before other steps.

# conda activate insilicoseq (https://stackoverflow.com/questions/34534513/calling-conda-source-activate-from-bash-script)
# The eval "$(conda shell.bash hook)" line initializes conda for shell interaction, which is necessary for using conda activate in a script. 
# After this line, you can use conda activate to activate your desired environment (comment by copilot).
# conda create -n omics python=3.14 -y
# conda activate omics
# conda install bioconda::insilicoseq
# further info & instructions https://insilicoseq.readthedocs.io/en/latest/iss/install.html
# conda install bioconda::seqtk


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

# # Task 2: Subsample raw reads

# for file in $OUT_DIR/*.fastq
# # for file in ~/ms/mg/03_reads/raw/*.fastq
# do
#     echo "Processing file: $file"
#     # Subsample 100000 reads from each FASTQ file
#     seqtk sample -s100 ${file} 100000 > $SUBSAMPLED_DIR/$(basename "$file")

# done

