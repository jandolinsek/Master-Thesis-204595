#!/bin/bash

# conda install bioconda::checkm-genome
# https://github.com/Ecogenomics/CheckM/wiki
# https://github.com/Ecogenomics/CheckM 
#

eval "$(conda shell.bash hook)"
conda activate checkm

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$2" # e.g. 8; positional argument

GENOMES=$BASEDIR/02_genomes/dereplicated/Dereplicated_Representative_Genomes
OUT_DIR=$BASEDIR/02_genomes/dereplicated/checkm 

checkm lineage_wf --tab_table --reduced_tree -t $THREADS $GENOMES $OUT_DIR
# checkm lineage_wf --tab_table -x fna --reduced_tree -t $THREADS $GENOMES $OUT_DIR
