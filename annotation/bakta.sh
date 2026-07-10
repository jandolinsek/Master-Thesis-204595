#!/bin/bash

# conda install bioconda::bakta
# https://github.com/oschwengers/bakta
# bakta is the recommended tool for prokaryotic genome annotation and replaces prokka

eval "$(conda shell.bash hook)"
conda activate bakta

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM_DIR="$2"  # megahit / metaspades; positional argument
THREADS="$3"

GENOMES=$ALGORITHM_DIR/01_binning/metabat2/fasta_bins
ANNOTATION_DIR=$ALGORITHM_DIR/02_annotation

# bakta_db download --output $DB_DIR --type light
# bakta_db download --output $DB_DIR --type full

DATABASE="/home/dolinsek/data/databases/bakta"

# Needs empty destination directory

COUNTER=1


for GENOME in $GENOMES/*.fa; do
    GENOME_NAME=$(basename $GENOME)
    echo "--------------"
    echo "Genome $COUNTER: $GENOME_NAME"
    echo "--------------"
    echo "File $COUNTER: $GENOME"
    echo "--------------"

    start_time=$(date +%s)

    bakta --db $DATABASE \
        --threads $THREADS \
        --prefix $GENOME_NAME \
        --output $ANNOTATION_DIR/$GENOME_NAME \
        --meta \
        --keep-contig-headers \
        "$GENOME"

        #         --compliant \


        COUNTER=$((COUNTER + 1))

    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "--------------"
    echo "Duration $elapsed_time seconds"
    echo "--------------"
    
done






      
