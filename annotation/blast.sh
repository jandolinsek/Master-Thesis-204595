#!/bin/bash

# conda install bioconda::blast
# https://blast.ncbi.nlm.nih.gov/doc/blast-help/

eval "$(conda shell.bash hook)"
conda activate blast

ASSEMBLY_DIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$2"

ANNOTATION_DIR=$ASSEMBLY_DIR/07_all_MAGs_genomes/annotation
OUTDIR=$ASSEMBLY_DIR/07_all_MAGs_genomes/annotation_expert
REF_PROTEINS=/home/dolinsek/01_metadata/cya_proteins.faa
REF_DB=/home/dolinsek/01_metadata/cya_db/cya_proteins_db

# makeblastdb -in "$REF_PROTEINS" -dbtype prot -out $REF_DB

for PROTEINS in $ANNOTATION_DIR/**/*.faa; do

  if [[ "$PROTEINS" != *hypotheticals* ]]; then

    echo "-------------------"
    echo "Translations: $PROTEINS"
    echo "-------------------"
    echo "Database: $REF_DB"
    echo "-------------------"

    NAME=$(basename "$(dirname "$PROTEINS")")
    blastp -query $PROTEINS \
          -db $REF_DB \
          -out $OUTDIR/"${NAME}_blastp_results.tsv" \
          -outfmt '6 qseqid sseqid pident qcovs length qlen slen qstart qend sstart send evalue bitscore' \
          -evalue 1e-20 \
          -max_target_seqs 10 \
          -num_threads $THREADS
  fi

done

# for HYPOTHETICALS in $ANNOTATIONS/**/*hypotheticals.faa; do

#   echo "-------------------"
#   echo "Translations: $HYPOTHETICALS"
#   echo "-------------------"
#   echo "Database: $REF_DB"
#   echo "-------------------"


#   NAME=$(basename "$(dirname "$HYPOTHETICALS")")
#   blastp -query $HYPOTHETICALS \
#         -db $REF_DB \
#         -out $OUTDIR/"${NAME}_hypotheticals_blastp_results.tsv" \
#         -outfmt '6 qseqid sseqid pident length qlen slen qstart qend sstart send evalue bitscore' \
#         -evalue 1e-20 \
#         -max_target_seqs 10 \
#         -num_threads $THREADS

# done



