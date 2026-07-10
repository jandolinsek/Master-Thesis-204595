#!/bin/bash

# conda install bioconda::bakta
# https://github.com/oschwengers/bakta
# https://github.com/oschwengers/bakta#protein-bulk-annotation - see when providing custonm protein db
# bakta is the recommended tool for prokaryotic genome annotation and replaces prokka

eval "$(conda shell.bash hook)"
conda activate bakta

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM_DIR="$2"  # megahit / metaspades; positional argument
THREADS="$3"

GENOMES=$ALGORITHM_DIR/06_HQ_MAGs_genomes/genomes
ANNOTATION_DIR=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation
# PROTEINS="/home/dolinsek/01_metadata/CYA_proteins.faa"

# bakta_db download --output $DB_DIR --type light
# bakta_db download --output $DB_DIR --type full

DATABASE="/home/dolinsek/data/databases/bakta"

# Needs empty destination directory

COUNTER=1

for GENOME in $GENOMES/*.fna; do
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
        --compliant \
        --keep-contig-headers \
         "$GENOME"
        # --proteins $PROTEINS \


        COUNTER=$((COUNTER + 1))

    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "--------------"
    echo "Duration $elapsed_time seconds"
    echo "--------------"

done


# for GENOME in $GENOMES/bin*.fa; do
#     GENOME_NAME=$(basename $GENOME)
#     echo "--------------"
#     echo "Genome $COUNTER: $GENOME_NAME"
#     echo "--------------"
#     echo "File $COUNTER: $GENOME"
#     echo "--------------"

#     start_time=$(date +%s)

#     bakta --db $DATABASE \
#         --threads $THREADS \
#         --prefix $GENOME_NAME \
#         --output $ANNOTATION_DIR/$GENOME_NAME \
#         --meta \
#         --keep-contig-headers \
#         "$GENOME"

#         #         --compliant \


#         COUNTER=$((COUNTER + 1))

#     end_time=$(date +%s)
#     elapsed_time=$((end_time - start_time))
#     echo "--------------"
#     echo "Duration $elapsed_time seconds"
#     echo "--------------"
    
# done