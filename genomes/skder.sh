#!/bin/bash

# conda install bioconda::skder
# conda install -c conda-forge "numpy<2.4" # downgrade numpy 

# https://github.com/raufs/skDER

eval "$(conda shell.bash hook)"
conda activate skder

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$2" # e.g. 40; positional argument

GENOMES=$BASEDIR/02_genomes/individual
GENOMES_DEREPLICATED_MULTIFASTA=$BASEDIR/02_genomes/dereplicated/genomes_multifasta.fasta
GENOMES_DEREPLICATED_DIR=$BASEDIR/02_genomes/dereplicated

skder -g $GENOMES \
     -o $GENOMES_DEREPLICATED_DIR \
     -i 99 \


     
for file in $GENOMES_DEREPLICATED_DIR/**/*.fna
do
  cat "$file" >> $GENOMES_DEREPLICATED_MULTIFASTA
done
