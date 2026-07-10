#!/bin/bash

# removing
# conda remove package
# conda remove --name <env_name> --all

# base
# conda install conda-forge::pigz
# conda install git


# # datasets
# conda create -n datasets
# eval "$(conda shell.bash hook)"
# conda activate datasets
# conda install -c conda-forge ncbi-datasets-cli
# conda install conda-forge::unzip
# conda deactivate

# # skder (dereplication)
# conda create -n skder
# eval "$(conda shell.bash hook)"
# conda activate skder
# conda install bioconda::skder
# conda install -c conda-forge "numpy<2.4" # downgrade numpy 
# conda install -c conda-forge "setuptools<70.0.0" -y
# conda install -c conda-forge time -y
# conda deactivate

# # qc
# conda create -n qc
# eval "$(conda shell.bash hook)"
# conda activate qc
# conda install bioconda::fastqc
# conda install bioconda::trimmomatic
# conda deactivate    

# # metaspades
# conda create -n spades
# eval "$(conda shell.bash hook)"
# conda activate spades
# conda install bioconda::spades
# conda deactivate
 
# # megahit
# conda create -n megahit
# eval "$(conda shell.bash hook)"
# conda activate megahit
# conda install bioconda::megahit
# conda deactivate

# # mapping
# conda create -n mapping
# eval "$(conda shell.bash hook)"
# conda activate mapping
# conda install bioconda::bowtie2
# conda install bioconda::samtools
# conda deactivate

# # metabat2
# conda create -n metabat2
# eval "$(conda shell.bash hook)"
# conda activate metabat2
# conda install bioconda::metabat2
# conda deactivate

# # semibin
# conda create -n semibin
# eval "$(conda shell.bash hook)"
# conda activate semibin
# conda install bioconda::semibin
# conda deactivate

# # checkm
# conda create -n checkm
# eval "$(conda shell.bash hook)"
# conda activate checkm
# conda install bioconda::checkm-genome
# conda install -n checkm -c conda-forge "setuptools<70.0.0" -y
# cd ~/miniconda3/envs/checkm/
# mkdir -p ~/checkm_data
# cd ~/checkm_data
# wget https://data.ace.uq.edu.au/public/CheckM_databases/checkm_data_2015_01_16.tar.gz # https://zenodo.org/record/7401545#.Y44ymHbMJD8
# tar -xzvf checkm_data_2015_01_16.tar.gz
# checkm data setRoot ~/miniconda3/envs/checkm/checkm_data
# rm checkm_data_2015_01_16.tar.gz
# cd
# conda deactivate

# # quast
# conda create -n quast
# eval "$(conda shell.bash hook)"
# conda activate quast
# conda install bioconda::quast
# conda deactivate

# bakta
# conda create -n bakta
# eval "$(conda shell.bash hook)"
# conda activate bakta
# conda install -c conda-forge -c bioconda bakta
# conda deactivate

# coverm
# conda create -n coverm
# eval "$(conda shell.bash hook)"
# conda activate coverm
# conda install bioconda::coverm
# conda install bioconda::bwa-mem2
# conda deactivate

# # dastool
# conda create -n dastool
# eval "$(conda shell.bash hook)"
# conda activate dastool
# conda install -c bioconda das_tool
# conda deactivate

# # skani
# conda create -n skani python -y
# eval "$(conda shell.bash hook)"
# conda activate skani
# conda install -c conda-forge pip setuptools numpy scipy matplotlib -y
# conda install bioconda::skani -y
# conda deactivate

# # jorg
# conda create -n jorg python -y
# eval "$(conda shell.bash hook)"
# conda activate jorg
# conda install -c conda-forge pip setuptools numpy scipy matplotlib -y
# conda install bioconda::mira
# conda install bioconda::bwa
# conda install bioconda::last
# conda install bioconda::seqtk
# conda install bioconda::pilon
# conda install bioconda::infernal
# cd ~/miniconda3/envs/jorg/ 
# git clone https://github.com/lmlui/Jorg.git
# conda install -c conda-forge boost=1.85.0 -y 
# conda deactivate

# # phylophlan
# conda create -n phylophlan python -y
# eval "$(conda shell.bash hook)"
# conda activate phylophlan
# conda install bioconda::phylophlan -y
# conda deactivate

# # gtdbtk
# conda create -n gtdbtk -y
# eval "$(conda shell.bash hook)"
# conda activate gtdbtk
# conda install bioconda::gtdbtk -y
# conda deactivate

# # bbmap
# conda create -n bbmap -y
# eval "$(conda shell.bash hook)"
# conda activate bbmap
# conda install bioconda::bbmap -y
# conda install bioconda::samtools -y
# conda install conda-forge::pigz -y
# conda deactivate

# # blast
# conda create -n blast -y
# eval "$(conda shell.bash hook)"
# conda activate blast
# conda install bioconda::blast -y
# conda deactivate

# # featurecounts
# conda create -n featurecounts -y
# eval "$(conda shell.bash hook)"
# conda activate featurecounts
# conda install bioconda::subread -y
# conda install bioconda::samtools -y
# conda deactivate

# # biopython
# conda create -n biopython -y
# eval "$(conda shell.bash hook)"
# conda activate biopython
# conda install conda-forge::biopython -y
# conda install conda-forge::pandas -y
# conda deactivate

# # graphlan
# conda create -n graphlan -y
# eval "$(conda shell.bash hook)"
# conda activate graphlan
# conda install -c bioconda graphlan -y
# conda deactivate

