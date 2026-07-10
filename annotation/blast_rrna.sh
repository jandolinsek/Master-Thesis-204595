#!/bin/bash

# conda install bioconda::blast
# https://blast.ncbi.nlm.nih.gov/doc/blast-help/

eval "$(conda shell.bash hook)"
conda activate blast

MTX_DIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
THREADS="$2"

ANNOTATION_DIR=$MTX_DIR/genomes/annotation
OUTDIR=$MTX_DIR/blast_rrna
REF_DNA=/home/dolinsek/01_metadata/rrna.ffn
REF_DB=/home/dolinsek/01_metadata/rrna_db

# makeblastdb -in "$REF_DNA" -dbtype nucl -out $REF_DB

for DNA in $ANNOTATION_DIR/**/*.ffn; do

  echo "-------------------"
  echo "Contigs: $DNA"
  echo "-------------------"
  echo "Database: $REF_DB"
  echo "-------------------"

  NAME=$(basename "$(dirname "$DNA")")
  blastn -query $DNA \
        -db $REF_DB \
        -out $OUTDIR/"${NAME}_blastn_results.tsv" \
        -outfmt '6 qseqid sseqid pident qcovs length qlen slen qstart qend sstart send evalue bitscore' \
        -evalue 1e-20 \
        -max_target_seqs 10 \
        -num_threads $THREADS

done


