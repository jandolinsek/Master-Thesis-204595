#!/bin/bash
# conda install bioconda::metabat2
# https://bitbucket.org/berkeleylab/metabat/src/master/

eval "$(conda shell.bash hook)"
conda activate metabat2

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
ALGORITHM="$2"  # megahit / metaspades; positional argument
THREADS="$3"  # number of threads; positional argument

echo ""
echo " --------- Algorithm: $ALGORITHM --------- "
echo ""

if [ $ALGORITHM == "megahit" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    ASSEMBLIES_FILE=$BASEDIR/05_assembly_megahit/00_assembly/assembly_full/final.contigs.fa
    COVERAGE_FILE=$BASEDIR/05_assembly_megahit/01_binning/bowtie2/coverage/depth_megahit.txt
    BAM_DIR=$BASEDIR/05_assembly_megahit/01_binning/bowtie2/bam
    BAMS=$(find $BAM_DIR -name "*.sorted.bam")
    jgi_summarize_bam_contig_depths --outputDepth $COVERAGE_FILE $BAMS 

elif [ $ALGORITHM == "metaspades" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    ASSEMBLIES_FILE=$BASEDIR/06_assembly_metaspades/00_assembly/assembly_full/contigs.fasta
    COVERAGE_FILE=$BASEDIR/06_assembly_metaspades/01_binning/bowtie2/coverage/depth_metaspades.txt
    BAM_DIR=$BASEDIR/06_assembly_metaspades/01_binning/bowtie2/bam
    BAMS=$(find $BAM_DIR -name "*.sorted.bam")
    jgi_summarize_bam_contig_depths --outputDepth $COVERAGE_FILE $BAMS 


elif [ $ALGORITHM == "metaspades_single" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    ASSEMBLIES_FILE=$BASEDIR/07_assembly_metaspades_single/00_assembly/assembly_single/concatenated/concatenated.fa.gz
    COVERAGE_FILE=$BASEDIR/07_assembly_metaspades_single/01_binning/bowtie2/coverage/depth_metaspades.txt
    BAM_DIR=$BASEDIR/07_assembly_metaspades_single/01_binning/bowtie2/bam
    BAMS=$(find $BAM_DIR -name "*.sorted.bam")
    jgi_summarize_bam_contig_depths --outputDepth $COVERAGE_FILE $BAMS 

else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades'."
    exit 1
fi


