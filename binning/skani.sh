#!/bin/bash

# conda install bioconda::skani
# https://github.com/bluenote-1577/skani

eval "$(conda shell.bash hook)"
conda activate skani

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM="$2"  # megahit / metaspades; positional argument
THREADS="$3" # e.g. 8; positional argument

SCRPITS_DIR="$HOME/00_scripts"
GENOMES=$BASEDIR/02_genomes/dereplicated/Dereplicated_Representative_Genomes/*.fna

CLUSTER_SIMILARITY=80
cd $SCRPITS_DIR


if [ $ALGORITHM == "megahit" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    SKANI_OUT=$BASEDIR/05_assembly_megahit/04_skani/results_skani.tsv 
    SKANI_OUT_TAB=$BASEDIR/05_assembly_megahit/04_skani/results_skani_tab.tsv 

    MAGS=$BASEDIR/05_assembly_megahit/01_binning/metabat2/fasta_bins/*.fa 

    skani triangle $GENOMES $MAGS -E -t $THREADS --medium -s 70 > $SKANI_OUT_TAB
    # skani triangle $GENOMES $MAGS -t $THREADS --medium -s 70 > $SKANI_OUT
    # python clustermap_triangle_mod.py $SKANI_OUT $CLUSTER_SIMILARITY $BASEDIR/05_assembly_megahit/04_skani



elif [ $ALGORITHM == "metaspades" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    SKANI_OUT=$BASEDIR/06_assembly_metaspades/04_skani/results_skani.tsv 
    SKANI_OUT_TAB=$BASEDIR/06_assembly_metaspades/04_skani/results_skani_tab.tsv 

    MAGS=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/fasta_bins/*.fa 

    skani triangle $GENOMES $MAGS -E -t $THREADS --medium -s 70 > $SKANI_OUT_TAB
    # skani triangle $GENOMES $MAGS -t $THREADS --medium -s 70 > $SKANI_OUT
    # python clustermap_triangle_mod.py $SKANI_OUT $CLUSTER_SIMILARITY $BASEDIR/06_assembly_metaspades/04_skani


else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades'."
    exit 1
fi


