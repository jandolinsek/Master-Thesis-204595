#!/bin/bash

# conda install bioconda::subread

# https://subread.sourceforge.net/featureCounts.html

eval "$(conda shell.bash hook)"
conda activate featurecounts

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ASSEMBLY_DIR="$2"  # megahit / metaspades; positional argument
DATA_DIR="$3"  # e.g. /home/jan/ms/1_mg/04_qc/trimmomatic_results; positional argument
THREADS="$4"

BAM_DIR=$DATA_DIR/mapped_reads
GFF_DIR=$ASSEMBLY_DIR/06_HQ_MAGs_genomes/annotation
# GFF_DIR=$ASSEMBLY_DIR/07_all_MAGs_genomes/annotation
# OUTDIR=$ASSEMBLY_DIR/06_HQ_MAGs_genomes/feature_counts
OUTDIR=$BASEDIR/07_MTX/feature_counts

# for GFF in $GFF_DIR/bin*/*.gff3; do
#     echo $GFF
#     grep -h 'NODE' $GFF >> $GFF_DIR/combined_annotations.gff3
# done

# for GFF in $GFF_DIR/GCA*/*.gff3; do
#     echo $GFF
#     grep -h -v '#' $GFF >> $GFF_DIR/combined_annotations.gff3
# done


BAM_LINKS=()

for BAM in $BAM_DIR/**/*sorted.bam; do

    SAMPLE=$(basename "$(dirname "$BAM")")
    BAM_NAME=$(echo $(basename $BAM))
    LINK=$BAM_DIR/links/$SAMPLE

    echo "-------------------"
    echo "File: $BAM"
    echo "-------------------"
    echo "Sample: $SAMPLE"
    echo "-------------------"
    echo "Link: $LINK"
    echo "-------------------"

    ## use samtools coverage only when counting mgx reads
    # samtools coverage $BAM > $OUTDIR/${SAMPLE}_contig_coverage.tsv

    ln -sf $BAM $LINK
    BAM_LINKS+=($LINK)

done

echo "-------------------"
echo "collection: ${BAM_LINKS[@]}"
echo "-------------------"

# run on concatenated annotations.



start_time=$(date +%s)

GFFS=$GFF_DIR/combined_annotations.gff3

# featureCounts \
#     -a $GFFS \
#     -p \
#     -B \
#     -F GFF \
#     -g Name \
#     -t CDS,tRNA,rRNA,ncRNA \
#     -T $THREADS \
#     --countReadPairs \
#     --verbose \
#     -o $OUTDIR/all_gene.txt \
#     "${BAM_LINKS[@]}" \
     

featureCounts \
    -a $GFFS \
    -p \
    -B \
    -F GFF \
    -t CDS \
    -g ID \
    -T $THREADS \
    --countReadPairs \
    --verbose \
    -o $OUTDIR/all.txt \
    "${BAM_LINKS[@]}" \

    #    -g Name \
     
    

end_time=$(date +%s)
elapsed_time=$((end_time - start_time))
echo "Duration $elapsed_time seconds" 


