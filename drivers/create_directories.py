#!/usr/bin/env python3

"""
Description: This script creates directories for the MGX & MTX pipeline. 

"""

import os

def create_directory_structure(base_dir, data_dir_mgx, data_dir_mtx):
    """
    Creates a comprehensive subdirectory structure for data analysis and storage.
    
    Generates processing and output directories under the base analysis folder, 
    as well as raw and intermediate read folders inside specific data paths for 
    both metagenomics (MGX) and metatranscriptomics (MTX).

    Args:
        base_dir (str): Path to the base directory where the main analysis 
            output structure will be initialized.
        data_dir_mgx (str): Path to the storage directory where MGX short-read 
            processing directories will be created.
        data_dir_mtx (str): Path to the storage directory where MTX short-read 
            processing directories will be created.

    Directory Structure Formatted:
        
        Data Storage MGX (data_dir_mgx/):
        ├── raw_reads/
        ├── trimmomatic_results/    
        ├── trimmomatic_results_subsampled/
        ├── mapped_reads/
        │   └── links/
        ├── concatenated_reads/
        └── concatenated_reads_subsampled/    

        Data Storage MTX (data_dir_mtx/):
        ├── raw_reads/
        ├── trimmomatic_results/    
        └── mapped_reads/
            └── links/

        Main Analysis Workspace (base_dir/):
        ├── 02_genomes/
        │   ├── individual/
        │   ├── multifasta/
        │   └── dereplicated/ (checkm, annotation, expert, phylogeny)
        ├── 04_qc/
        │   ├── fastqc_results_MGX/
        │   └── fastqc_results_MTX/
        ├── 05_assembly_megahit/ & 06_assembly_metaspades/
        │   ├── 00_assembly/ (subsampled, full, single)
        │   ├── 01_binning/ (bowtie2, metabat2, semibin2, checkm, quast)
        │   ├── 02_annotation/
        │   ├── 03_mapping/ (bbmap, coverm, instrain)
        │   ├── 04_skani/
        │   ├── 05_phylogeny/
        │   └── 06_HQ_MAGs_genomes/ & 07_all_MAGs_genomes/
        └── 07_MTX/ (genomes, blast_rrna, feature_counts)

    Raises:
        OSError: If permission is denied or a directory cannot be written.

   """

    # Define the directory structure
    directories = [

        os.path.join(data_dir_mgx, 'raw_reads'),
        os.path.join(data_dir_mgx, 'trimmomatic_results'),
        os.path.join(data_dir_mgx, 'trimmomatic_results_subsampled'),
        os.path.join(data_dir_mgx, 'mapped_reads'),
        os.path.join(data_dir_mgx, 'mapped_reads', 'links'),
        os.path.join(data_dir_mgx, 'concatenated_reads'),
        os.path.join(data_dir_mgx, 'concatenated_reads_subsampled'),

        os.path.join(data_dir_mtx, 'raw_reads'),
        os.path.join(data_dir_mtx, 'trimmomatic_results'),
        os.path.join(data_dir_mtx, 'mapped_reads'),
        os.path.join(data_dir_mtx, 'mapped_reads', 'links'),


        os.path.join(base_dir, '02_genomes'), 
        os.path.join(base_dir, '02_genomes', 'individual'),
        os.path.join(base_dir, '02_genomes', 'multifasta'),
        os.path.join(base_dir, '02_genomes', 'dereplicated'),
        os.path.join(base_dir, '02_genomes', 'dereplicated', 'checkm'),
        os.path.join(base_dir, '02_genomes', 'dereplicated', 'annotation'),
        os.path.join(base_dir, '02_genomes', 'dereplicated', 'annotation_expert'),
        os.path.join(base_dir, '02_genomes', 'dereplicated', 'phylogeny'),

        os.path.join(base_dir, '04_qc'),
        os.path.join(base_dir, '04_qc', 'fastqc_results_MGX'),
        os.path.join(base_dir, '04_qc', 'fastqc_results_MTX'),

        
        os.path.join(base_dir, '05_assembly_megahit'),
        os.path.join(base_dir, '05_assembly_megahit', '00_assembly'),
        os.path.join(base_dir, '05_assembly_megahit', '00_assembly', 'assembly_subsampled'), 
        os.path.join(base_dir, '05_assembly_megahit', '00_assembly', 'assembly_full'),  
        os.path.join(base_dir, '05_assembly_megahit', '01_binning'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'bowtie2'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'bowtie2', 'bam'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'bowtie2', 'coverage'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'bowtie2', 'index'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'metabat2'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'metabat2', 'fasta_bins'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'semibin2'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'checkm'),
        os.path.join(base_dir, '05_assembly_megahit', '01_binning', 'quast'),
        os.path.join(base_dir, '05_assembly_megahit', '02_annotation'),
        os.path.join(base_dir, '05_assembly_megahit', '03_mapping'),
        os.path.join(base_dir, '05_assembly_megahit', '03_mapping', 'bbmap'),
        os.path.join(base_dir, '05_assembly_megahit', '03_mapping', 'coverm'),
        os.path.join(base_dir, '05_assembly_megahit', '03_mapping', 'instrain'),
        os.path.join(base_dir, '05_assembly_megahit', '04_skani'),
        os.path.join(base_dir, '05_assembly_megahit', '05_phylogeny'),
        os.path.join(base_dir, '05_assembly_megahit', '06_HQ_MAGs_genomes'),
        os.path.join(base_dir, '05_assembly_megahit', '06_HQ_MAGs_genomes', 'genomes'),
        os.path.join(base_dir, '05_assembly_megahit', '06_HQ_MAGs_genomes', 'genomes_cleaned'),
        os.path.join(base_dir, '05_assembly_megahit', '06_HQ_MAGs_genomes', 'annotation'),
        os.path.join(base_dir, '05_assembly_megahit', '06_HQ_MAGs_genomes', 'annotation_expert'),
        os.path.join(base_dir, '05_assembly_megahit', '06_HQ_MAGs_genomes', 'feature_counts'),
        os.path.join(base_dir, '05_assembly_megahit', '07_all_MAGs_genomes'),
        os.path.join(base_dir, '05_assembly_megahit', '07_all_MAGs_genomes', 'genomes'),
        os.path.join(base_dir, '05_assembly_megahit', '07_all_MAGs_genomes', 'genomes_cleaned'),
        os.path.join(base_dir, '05_assembly_megahit', '07_all_MAGs_genomes', 'annotation'),
        os.path.join(base_dir, '05_assembly_megahit', '07_all_MAGs_genomes', 'annotation_expert'),
        os.path.join(base_dir, '05_assembly_megahit', '07_all_MAGs_genomes', 'feature_counts'),       

        os.path.join(base_dir, '06_assembly_metaspades'),
        os.path.join(base_dir, '06_assembly_metaspades', '00_assembly'),
        os.path.join(base_dir, '06_assembly_metaspades', '00_assembly', 'assembly_subsampled'),
        os.path.join(base_dir, '06_assembly_metaspades', '00_assembly', 'assembly_full'),
        os.path.join(base_dir, '06_assembly_metaspades', '00_assembly', 'assembly_single'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2', 'bam'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2', 'coverage'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2', 'index'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2_single'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2_single', 'bam'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2_single', 'coverage'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'bowtie2_single', 'index'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'metabat2'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'metabat2', 'fasta_bins'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'semibin2'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'checkm'),
        os.path.join(base_dir, '06_assembly_metaspades', '01_binning', 'quast'),
        os.path.join(base_dir, '06_assembly_metaspades', '02_annotation'),
        os.path.join(base_dir, '06_assembly_metaspades', '03_mapping'),
        os.path.join(base_dir, '06_assembly_metaspades', '03_mapping', 'bbmap'),
        os.path.join(base_dir, '06_assembly_metaspades', '03_mapping', 'coverm'),
        os.path.join(base_dir, '06_assembly_metaspades', '03_mapping', 'instrain'),
        os.path.join(base_dir, '06_assembly_metaspades', '04_skani'),
        os.path.join(base_dir, '06_assembly_metaspades', '05_phylogeny'),
        os.path.join(base_dir, '06_assembly_metaspades', '06_HQ_MAGs_genomes'),
        os.path.join(base_dir, '06_assembly_metaspades', '06_HQ_MAGs_genomes', 'genomes'),
        os.path.join(base_dir, '06_assembly_metaspades', '06_HQ_MAGs_genomes', 'genomes_cleaned'),
        os.path.join(base_dir, '06_assembly_metaspades', '06_HQ_MAGs_genomes', 'annotation'),
        os.path.join(base_dir, '06_assembly_metaspades', '06_HQ_MAGs_genomes', 'annotation_expert'),
        os.path.join(base_dir, '06_assembly_metaspades', '06_HQ_MAGs_genomes', 'feature_counts'),
        os.path.join(base_dir, '06_assembly_metaspades', '07_all_MAGs_genomes'),
        os.path.join(base_dir, '06_assembly_metaspades', '07_all_MAGs_genomes', 'genomes'),
        os.path.join(base_dir, '06_assembly_metaspades', '07_all_MAGs_genomes', 'genomes_cleaned'),
        os.path.join(base_dir, '06_assembly_metaspades', '07_all_MAGs_genomes', 'annotation'),
        os.path.join(base_dir, '06_assembly_metaspades', '07_all_MAGs_genomes', 'annotation_expert'),
        os.path.join(base_dir, '06_assembly_metaspades', '07_all_MAGs_genomes', 'feature_counts'),        
     
        os.path.join(base_dir, '07_MTX'),
        os.path.join(base_dir, '07_MTX', 'genomes'),
        os.path.join(base_dir, '07_MTX', 'blast_rrna'),
        os.path.join(base_dir, '07_MTX', 'feature_counts'),



    ]

    # Create the directories
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")


sample_names = ["1", "9", "SO4"]

for sample_name in sample_names:
    # Step 1: Create the directory structure
    base_directory = f"/home/dolinsek/{sample_name}_mgenomics"
    data_directory_mgx = f"/home/dolinsek/data/reads_mg/{sample_name}"
    data_directory_mtx = f"/home/dolinsek/data/Metatranscriptomics/{sample_name}"

    create_directory_structure(base_directory, data_directory_mgx, data_directory_mtx)

print("Directory structure created.")