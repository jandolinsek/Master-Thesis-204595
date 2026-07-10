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
    OUT_FILES=$BASEDIR/05_assembly_megahit/01_binning/metabat2/bins/bin
    OUT_FASTA=$BASEDIR/05_assembly_megahit/01_binning/metabat2/fasta_bins/bin
    OUT_DIR=$BASEDIR/05_assembly_megahit/01_binning/metabat2/
    OUT_BINS=$BASEDIR/05_assembly_megahit/01_binning/metabat2/bins.txt

    # -l flag provides only contig names, not fastas

    metabat2 -i ${ASSEMBLIES_FILE} -a ${COVERAGE_FILE} -o ${OUT_FASTA} -m 1500 -t $THREADS
    mv ${OUT_FASTA}.BinInfo.txt ${OUT_DIR}

elif [ $ALGORITHM == "metaspades" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    ASSEMBLIES_FILE=$BASEDIR/06_assembly_metaspades/00_assembly/assembly_full/contigs.fasta
    COVERAGE_FILE=$BASEDIR/06_assembly_metaspades/01_binning/bowtie2/coverage/depth_metaspades.txt
    OUT_FILES=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/bins/bin
    OUT_FASTA=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/fasta_bins/bin
    OUT_DIR=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/
    # OUT_BINS=$BASEDIR/06_assembly_metaspades/01_binning/metabat2/bins.txt

    # -l flag provides only contig names, not fastas

    metabat2 -i ${ASSEMBLIES_FILE} -a ${COVERAGE_FILE} -o ${OUT_FASTA} -m 1500 -t $THREADS
    mv ${OUT_FASTA}.BinInfo.txt ${OUT_DIR}

elif [ $ALGORITHM == "metaspades_single" ]; then

    echo ""
    echo " --------- Algorithm confirmed: $ALGORITHM --------- "
    echo ""

    ASSEMBLIES_FILE=$BASEDIR/07_assembly_metaspades_single/00_assembly/assembly_single/concatenated/concatenated.fa.gz
    COVERAGE_FILE=$BASEDIR/07_assembly_metaspades_single/01_binning/bowtie2/coverage/depth_metaspades.txt
    OUT_FILES=$BASEDIR/07_assembly_metaspades_single/01_binning/metabat2/bins/bin
    OUT_FASTA=$BASEDIR/07_assembly_metaspades_single/01_binning/metabat2/fasta_bins/bin
    OUT_DIR=$BASEDIR/07_assembly_metaspades_single/01_binning/metabat2/
    # OUT_BINS=$BASEDIR/07_assembly_metaspades_single/01_binning/metabat2/bins.txt

    # -l flag provides only contig names, not fastas

    metabat2 -i ${ASSEMBLIES_FILE} -a ${COVERAGE_FILE} -o ${OUT_FASTA} -m 1500 -t $THREADS
    mv ${OUT_FASTA}.BinInfo.txt ${OUT_DIR}

else
    echo "Invalid algorithm specified. Use 'megahit' or 'metaspades'."
    exit 1
fi




# > $OUT_BINS  # empty the output file first

# for f in ${OUT_DIR}bins/*; do
#   num=$(basename "$f" | awk -F. '{print $2}')
#   awk -v num="$num" '{print $1 "\t" num}' "$f" >> "$OUT_BINS"
# done