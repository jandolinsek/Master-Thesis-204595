#!/bin/bash

# conda install bioconda::bbmap
# conda install bioconda::samtools

# https://bbmap.org/

eval "$(conda shell.bash hook)"
conda activate bbmap

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ASSEMBLY_DIR="$2"  # megahit / metaspades; positional argument
DATA_DIR="$3"  # e.g. /home/jan/ms/1_mg/04_qc/trimmomatic_results; positional argument
THREADS="$4"

# BBSCRIPTS=/home/jan/miniconda3/envs/bbmap/bin
READ_DIR=$DATA_DIR/trimmomatic_results/PE/
GENOMES=$ASSEMBLY_DIR/07_all_MAGs_genomes/genomes
GENOMES_CLEAN=$ASSEMBLY_DIR/07_all_MAGs_genomes/genomes_cleaned


# # Removes any chars in fasta header after the first whitespace, which is important for featureCounts to work properly
# for GENOME in $GENOMES/*.fna; do

#     NAME=$(basename -s .fna $GENOME)
#     echo "-------------------"
#     echo "Sample: $NAME"
#     echo "-------------------"
#     reformat.sh in=$GENOME out=$GENOMES_CLEAN/${NAME}.fna trd

# done

# # Removes any chars in fasta header after the first whitespace, which is important for featureCounts to work properly
# for GENOME in $GENOMES/*.fa; do

#     NAME=$(basename -s .fa $GENOME)
#     echo "-------------------"
#     echo "Sample: $NAME"
#     echo "-------------------"
#     reformat.sh in=$GENOME out=$GENOMES_CLEAN/${NAME}.fna trd

# done


# iterate over all R1 files named *_1.fq.gz under READDIR and its subdirectories
for READ1 in $READ_DIR/**/*_1.fq.gz; do
    
    READ2=$(echo $READ1 | sed "s/_1.fq.gz/_2.fq.gz/")        
    READ_NAME=$(echo $(basename $(dirname $READ1)))

    start_time=$(date +%s)
    OUTDIR=$DATA_DIR/mapped_reads/$READ_NAME


    mkdir -p $OUTDIR
    cd $OUTDIR

    # if runnning low on mem, use usemodulo flag

    # ambiguous=all; something to consider
    bbsplit.sh ref=$GENOMES_CLEAN \
        in=$READ1 \
        in2=$READ2 \
        out=$OUTDIR/MAGs_genomes.bam \
        unpigz=f \
        touppercase=t \
        slow=f \
        threads=$THREADS \
        ambiguous=best \
        ambiguous2=best


    samtools sort $OUTDIR/MAGs_genomes.bam -o $OUTDIR/MAGs_genomes_sorted.bam -@ $THREADS
    samtools index $OUTDIR/MAGs_genomes_sorted.bam -@ $THREADS

    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "Duration $elapsed_time seconds" 

done

