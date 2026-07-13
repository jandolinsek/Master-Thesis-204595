#!/bin/bash

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument

ANNOTATION_BAKTA=$BASEDIR/07_MTX/genomes/annotation
ANNOTATION_BLAST=$BASEDIR/07_MTX/genomes/annotation_expert
OUTDIR=$BASEDIR/07_MTX/feature_counts


for ANNOTATION in $ANNOTATION_BAKTA/**/*.fna.tsv; do
    echo $ANNOTATION
    grep -h -v '#' $ANNOTATION >> $OUTDIR/combined_features.tsv
done

for ANNOTATION in $ANNOTATION_BAKTA/**/*.fa.tsv; do
    echo $ANNOTATION
    grep -h -v '#' $ANNOTATION >> $OUTDIR/combined_features.tsv
done


# for ANNOTATION in $ANNOTATION_BLAST/*blastp_results.tsv; do
#     echo $ANNOTATION
#     grep -h -v '#' $ANNOTATION >> $OUTDIR/combined_features_blast.tsv
# done

