#!/bin/bash

# conda install bioconda::bakta
# https://github.com/oschwengers/bakta
# bakta is the recommended tool for prokaryotic genome annotation and replaces prokka

eval "$(conda shell.bash hook)"
conda activate bakta

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$2"

# bakta_db download --output $DB_DIR --type light
# bakta_db download --output $DB_DIR --type full

DATABASE="/home/dolinsek/data/databases/bakta"

GENOMES=$BASEDIR/02_genomes/dereplicated/Dereplicated_Representative_Genomes/*.fna
ANNOTATION_DIR=$BASEDIR/02_genomes/dereplicated/annotation
N=1

# for GENOME in $GENOMES; do

#     GENOME_NAME=$(basename "$GENOME" .fna)
#     echo "--------------"
#     echo "Genome $N: $GENOME_NAME"
#     echo "--------------"
#     echo "File $N: $GENOME"
#     echo "--------------"

#     bakta --db $DATABASE \
#         --threads $THREADS \
#         --prefix $GENOME_NAME \
#         --output $ANNOTATION_DIR/$GENOME_NAME \
#         --meta \
#         --compliant \
#         --keep-contig-headers \
#         "$GENOME"

#         N=$N+1
# done


GENOME="/home/dolinsek/1_mgenomics/06_assembly_metaspades/06_HQ_MAGs_genomes/GCA_977008005.1_Pseudomonas_sp._R-92830_assembly_genomic.fna"


GENOME_NAME=$(basename "$GENOME" .fna)
echo "--------------"
echo "Genome $N: $GENOME_NAME"
echo "--------------"
echo "File $N: $GENOME"
echo "--------------"

ANNOTATION_DIR="/home/dolinsek/1_mgenomics/06_assembly_metaspades/06_HQ_MAGs_genomes/annotation"

bakta --db $DATABASE \
    --threads $THREADS \
    --prefix $GENOME_NAME \
    --output $ANNOTATION_DIR/$GENOME_NAME \
    --meta \
    --compliant \
    --keep-contig-headers \
    --force\
    "$GENOME"


      
