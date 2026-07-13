#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate biopython

# conda install conda-forge::biopython

# in_fasta = file = sys.argv[1]
# in_blast_table = sys.argv[2]
# out_fasta_cyn = sys.argv[3]
# out_fasta_all = sys.argv[4]
# in_ref_proteins = sys.argv[5]

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM_DIR="$2"  # megahit / metaspades; positional argument

SCRIPTS_DIR="/home/dolinsek/00_scripts"
ANNOTATION_DIR=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation
REFERENCE_TABLE="/home/dolinsek/01_metadata/CYA_genes_expert.tsv"

cd $SCRIPTS_DIR

COUNTER=1


for ANNOTATION in $ANNOTATION_DIR/**/*hypotheticals.faa; do

    mv $ANNOTATION ${ANNOTATION}.hypothetical
    echo "--------------"
    echo "Moving hypotheticals $COUNTER: $ANNOTATION"
    echo "--------------"
    COUNTER=$((COUNTER + 1))

done

COUNTER=1

for ANNOTATION in $ANNOTATION_DIR/**/*.faa; do

        ANNOTATION_NAME=$(basename "$(dirname "$ANNOTATION")")

        echo "--------------"
        echo "Annotation $COUNTER: $ANNOTATION_NAME"
        echo "--------------"

        OUTPUT_EXPERT=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation_expert/${ANNOTATION_NAME}_expert_only.faa
        OUTPUT_EXPERT_ALL=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation_expert/${ANNOTATION_NAME}.faa
        BLAST_TABLE=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation_expert/"${ANNOTATION_NAME}_blastp_results.tsv"

        python reannotation_expert.py $ANNOTATION $BLAST_TABLE $OUTPUT_EXPERT $OUTPUT_EXPERT_ALL $REFERENCE_TABLE

        COUNTER=$((COUNTER + 1))

done

for ANNOTATION in $ANNOTATION_DIR/**/*.ffn; do

        ANNOTATION_NAME=$(basename "$(dirname "$ANNOTATION")")

        echo "--------------"
        echo "Annotation $COUNTER: $ANNOTATION_NAME"
        echo "--------------"

        OUTPUT_EXPERT=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation_expert/${ANNOTATION_NAME}_expert_only.ffn
        OUTPUT_EXPERT_ALL=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation_expert/${ANNOTATION_NAME}.ffn
        BLAST_TABLE=$ALGORITHM_DIR/06_HQ_MAGs_genomes/annotation_expert/"${ANNOTATION_NAME}_blastp_results.tsv"

        python reannotation_expert.py $ANNOTATION $BLAST_TABLE $OUTPUT_EXPERT $OUTPUT_EXPERT_ALL $REFERENCE_TABLE

        COUNTER=$((COUNTER + 1))

done
