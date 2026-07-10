#!/bin/bash

READ_DIR="$1" # e.g. /home/jan/ms/1_mg; positional argument

SEQ_DIR=${READ_DIR}/trimmomatic_results/PE
OUT_DIR=${READ_DIR}/concatenated_reads

READ1=_1.fq.gz
READ2=_2.fq.gz

# make a list of the files in the SEQ_DIR
find ${SEQ_DIR} -name "*${READ1}" -o -name "*${READ2}" > ${OUT_DIR}/sample_files.txt

# for assembly with spades, note that "Currently metaSPAdes supports only a single short-read library which has to be paired-end "
# thus, we need to concatenate all the R1 and R2 files into one file each...
# Gzip files can be safely concatenated directly without decompressing and recompressing:
cat $(grep "${READ1}$" "${OUT_DIR}/sample_files.txt") > "${OUT_DIR}/all_R1_PE_full.fq.gz"
cat $(grep "${READ2}$" "${OUT_DIR}/sample_files.txt") > "${OUT_DIR}/all_R2_PE_full.fq.gz" 
