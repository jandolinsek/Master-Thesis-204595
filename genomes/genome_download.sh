#!/bin/bash

# conda install -c conda-forge ncbi-datasets-cli
# conda install conda-forge::unzip

eval "$(conda shell.bash hook)"
conda activate datasets

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
SAMPLE_NAME="$2" # e.g. 1; positional argument

GENOMES=$HOME/01_metadata/genome_accessions_$SAMPLE_NAME.txt
GENOMES_DIR=$BASEDIR/02_genomes/individual
GENOMES_MULTIFASTA=$BASEDIR/02_genomes/multifasta/genomes_multifasta.fasta

mkdir -p tmp
cd tmp

# download genomes listed in ~/ms/mg/genome_accessions.txt, replace files when prompted
for accession in $(cat $GENOMES)
do
  datasets download genome accession $accession --include genome
  unzip -o ncbi_dataset.zip
done

# move all the files to a new folder genomes
find ncbi_dataset/ -type f -exec mv {} $GENOMES_DIR \;

# now merge them into multifasta
for file in $GENOMES_DIR/*.fna
do
  cat "$file" >> $GENOMES_MULTIFASTA
done

cd ..
rm -r tmp