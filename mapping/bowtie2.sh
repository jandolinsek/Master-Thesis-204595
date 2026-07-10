#!/bin/bash

# conda install bioconda::bowtie2
# conda install bioconda::samtools
# 

eval "$(conda shell.bash hook)"
conda activate mapping

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM="$2"  # megahit / metaspades; positional argument
READ_DIR_BASE="$3" # e.g. /home/data; positional argument
THREADS="$4"

READ_DIR=$READ_DIR_BASE/trimmomatic_results/PE

# ASSEMBLIES_FILE_SUBSAMPLED=$BASEDIR/05_assembly/metaspades_subsampled/contigs.fasta
# ASSEMBLIES_FILE_FULL=$BASEDIR/05_assembly/metaspades_full/contigs.fasta

echo ""
echo " --------- Algorithm: $ALGORITHM --------- "
echo ""

if [ $ALGORITHM == "megahit" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    ASSEMBLIES_FILE=$BASEDIR/05_assembly_megahit/00_assembly/assembly_full/final.contigs.fa
    BI_FILE=$BASEDIR/05_assembly_megahit/01_binning/bowtie2/index
    OUT_DIR=$BASEDIR/05_assembly_megahit/01_binning/bowtie2/bam

elif [ $ALGORITHM == "metaspades" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""
    
    ASSEMBLIES_FILE=$BASEDIR/06_assembly_metaspades/00_assembly/assembly_full/contigs.fasta
    BI_FILE=$BASEDIR/06_assembly_metaspades/01_binning/bowtie2/index
    OUT_DIR=$BASEDIR/06_assembly_metaspades/01_binning/bowtie2/bam

elif [ $ALGORITHM == "metaspades_single" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""
    
    ASSEMBLIES_FILE=$BASEDIR/07_assembly_metaspades_single/00_assembly/assembly_single/concatenated/concatenated.fa.gz
    BI_FILE=$BASEDIR/07_assembly_metaspades_single/01_binning/bowtie2/index
    OUT_DIR=$BASEDIR/07_assembly_metaspades_single/01_binning/bowtie2/bam


elif [ $ALGORITHM == "metaspades_re" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""
    
    ASSEMBLIES_FILE=$BASEDIR/08_skani/01_clusters/cluster_1_combined.fa
    BI_FILE=$BASEDIR/08_skani/01_clusters/cl1_rebowtie2/index
    OUT_DIR=$BASEDIR/08_skani/01_clusters/cl1_rebowtie2/bam

else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades' or 'metaspades_single'."
    exit 1
fi

echo "file: $ASSEMBLIES_FILE"


# Build Bowtie2 index 
bowtie2-build $ASSEMBLIES_FILE $BI_FILE --threads $THREADS 

# Loop through all paired-end read sets
for READ1 in $READ_DIR/**/*_1.fq.gz; do

    READ2=$(echo $READ1 | sed "s/_1.fq.gz/_2.fq.gz/")
    READ_NAME=$(echo $(basename $(dirname "$READ1")))

    start_time=$(date +%s)

    echo ""
    echo "------------ Mapping $READ_NAME with Bowtie2 ------------ "    
    echo ""
    
    # there can be issues with the paired-end reads, check numbers, only few align
    bowtie2 -x ${BI_FILE} \
        -1 "$READ1" -2 "$READ2" \
        --very-sensitive \
        -S "$OUT_DIR/$READ_NAME.sam"\
        -p $THREADS \
        --quiet

    samtools view -bS "$OUT_DIR/$READ_NAME.sam" | samtools sort -o "$OUT_DIR/$READ_NAME.sorted.bam"
    samtools index "$OUT_DIR/$READ_NAME.sorted.bam"
    rm "$OUT_DIR/$READ_NAME.sam"

    end_time=$(date +%s)
    elapsed_time=$((end_time - start_time))
    echo "Duration $elapsed_time seconds" 
done


