#!/bin/bash

# conda install bioconda::gtdbtk
# https://ecogenomics.github.io/GTDBTk/

eval "$(conda shell.bash hook)"
conda activate gtdbtk

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$2"

GENOMES=$BASEDIR/02_genomes/dereplicated/Dereplicated_Representative_Genomes
OUT_DIR_GENOMES=$BASEDIR/02_genomes/dereplicated/phylogeny 

gtdbtk classify_wf --genome_dir $GENOMES --extension '.fna' --out_dir $OUT_DIR_GENOMES --cpus $THREADS



      
