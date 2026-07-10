#!/bin/bash
# conda install bioconda::megahit

# https://github.com/voutcn/MEGAHIT
# https://github.com/voutcn/megahit/wiki

eval "$(conda shell.bash hook)"
conda activate megahit

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
READ_DIR="$2/trimmomatic_results/PE" # e.g. /home/reads_mg/1; positional argument
THREADS="$3" # e.g. 8; positional argument

OUT_DIR=$BASEDIR/05_assembly_megahit/00_assembly/assembly_full

# loop over all files in that directory and its subdirectories
READS1=""
READS2=""

for READ1 in $READ_DIR/**/*_1.fq.gz; do

    READ2=$(echo $READ1 | sed "s/_1.fq.gz/_2.fq.gz/")

    READS1="${READS1}${READ1},"
    READS2="${READS2}${READ2},"
done

READS1=${READS1%,}
READS2=${READS2%,}

# echo "READS1: $READS1"
# echo "READS2: $READS2"

start_time=$(date +%s)

megahit -1 $READS1 \
        -2 $READS2 \
        -o $OUT_DIR -t $THREADS -f

end_time=$(date +%s)
elapsed_time=$((end_time - start_time))
echo "Duration $elapsed_time seconds"