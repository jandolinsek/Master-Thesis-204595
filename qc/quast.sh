#!/bin/bash

# conda install bioconda::quast
# https://quast.sourceforge.net/docs/manual.html#sec2

eval "$(conda shell.bash hook)"
conda activate quast

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM="$2"  # megahit / metaspades; positional argument
THREADS="$3" # e.g. 8; positional argument

GENOMES_DEREPLICATED_MULTIFASTA=$BASEDIR/02_genomes/dereplicated/genomes_multifasta.fasta

echo "Algorithm: $ALGORITHM"

if [[ $ALGORITHM == "megahit" ]]; then
    BIN_DIR=$BASEDIR/05_assembly_megahit/01_binning/metabat2/fasta_bins
    OUT_DIR=$BASEDIR/05_assembly_megahit/01_binning/quast

    echo "Algorithm confirmed - megahit"

elif [[ $ALGORITHM == "metaspades" ]]; then
    BIN_DIR=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/fasta_bins
    OUT_DIR=$BASEDIR/06_assembly_metaspades/01_binning/quast

    echo "Algorithm confirmed - metaspades"

else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades'."
    exit 1
fi

metaquast $BIN_DIR/*.fa \
    -r $GENOMES_DEREPLICATED_MULTIFASTA \
    -o $OUT_DIR \
    -t $THREADS \
    --silent



