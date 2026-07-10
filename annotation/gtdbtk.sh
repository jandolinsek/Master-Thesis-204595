#!/bin/bash

# conda install bioconda::gtdbtk
# https://ecogenomics.github.io/GTDBTk/

eval "$(conda shell.bash hook)"
conda activate gtdbtk

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM="$2"  # megahit / metaspades; positional argument
THREADS="$3"


echo ""
echo " --------- Algorithm: $ALGORITHM --------- "
echo ""

if [ $ALGORITHM == "megahit" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    BIN_DIR=$BASEDIR/05_assembly_megahit/01_binning/metabat2/fasta_bins
    OUT_DIR_BINS=$BASEDIR/05_assembly_megahit/05_phylogeny

    gtdbtk classify_wf --genome_dir $BIN_DIR --out_dir $OUT_DIR_BINS --cpus $THREADS

elif [ $ALGORITHM == "metaspades" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    BIN_DIR=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/fasta_bins
    OUT_DIR_BINS=$BASEDIR/06_assembly_metaspades/05_phylogeny

    gtdbtk classify_wf --genome_dir $BIN_DIR --extension '.fa' --out_dir $OUT_DIR_BINS --cpus $THREADS

else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades' or 'metaspades_single'."
    exit 1
fi

      
