#!/bin/bash

# conda install bioconda::checkm-genome
# https://github.com/Ecogenomics/CheckM/wiki
# https://github.com/Ecogenomics/CheckM 
#

eval "$(conda shell.bash hook)"
conda activate checkm

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM="$2"  # megahit / metaspades; positional argument
THREADS="$3" # e.g. 8; positional argument

echo "Algorithm: $ALGORITHM"

if [[ $ALGORITHM == "megahit" ]]; then
    BIN_DIR=$BASEDIR/05_assembly_megahit/01_binning/metabat2/fasta_bins
    OUT_DIR=$BASEDIR/05_assembly_megahit/01_binning/checkm

    echo "Algorithm confirmed - megahit"

elif [[ $ALGORITHM == "metaspades" ]]; then
    BIN_DIR=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/fasta_bins
    OUT_DIR=$BASEDIR/06_assembly_metaspades/01_binning/checkm

    echo "Algorithm confirmed - metaspades"

else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades'."
    exit 1
fi

checkm lineage_wf --tab_table -x fa --reduced_tree -t $THREADS $BIN_DIR $OUT_DIR/
