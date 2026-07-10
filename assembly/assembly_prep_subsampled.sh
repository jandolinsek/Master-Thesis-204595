#!/bin/bash

BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument

SEQ_DIR=${BASEDIR}/04_qc/trimmomatic_results_subsampled/PE

OUT_DIR=${BASEDIR}/04_qc/concatenated_reads_subsampled

READ1_SUBSAMPLED=_1.fq.gz
READ2_SUBSAMPLED=_2.fq.gz

# make a list of the files in the SEQ_DIR
find ${SEQ_DIR} -name "*${READ1_SUBSAMPLED}" -o -name "*${READ2_SUBSAMPLED}" > ${OUT_DIR}/sample_files_subsampled.txt

# for assembly with spades, note that "Currently metaSPAdes supports only a single short-read library which has to be paired-end "
# thus, we need to concatenate all the R1 and R2 files into one file each...
gunzip -c $(grep "${READ1_SUBSAMPLED}$" ${OUT_DIR}/sample_files_subsampled.txt) > ${OUT_DIR}/all_R1_PE_subsampled.fastq
gunzip -c $(grep "${READ2_SUBSAMPLED}$" ${OUT_DIR}/sample_files_subsampled.txt) > ${OUT_DIR}/all_R2_PE_subsampled.fastq
