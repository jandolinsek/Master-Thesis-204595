#!/bin/bash


tar -xvf "your_file.tar.gz" -C "your_output_directory"

# look into seqs
zcat sample.fastq.gz | head -n 40

FILE="//x1hbrnas1/raw_data/Novogene/MIBIREM/Metatranscriptomics/Novogene_seq_new/X208SC25120714-Z01-F001.tar"
DEST=

scp -P 12121 -i ~/.ssh/id_ed25519 $FILE dolinsek@i121srv03.vu-wien.ac.at:/data/Metatranscriptomics/

scp -r -P 12121 -i ~/.ssh/id_ed25519 /local/path/dir user@server:/remote/path/


# in powershell
# cd \\x1hbrnas1\raw_data\Novogene\MIBIREM\Metatranscriptomics\Novogene_seq_new
# scp -P 12121 -i c:\Users\dolinsekj\.ssh\id_rsa X208SC25120714-Z01-F001.tar dolinsek@i121srv03.vu-wien.ac.at:/home/dolinsek/data/Metatranscriptomics/



