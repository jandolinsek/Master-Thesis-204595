#!/usr/bin/env python3

"""
Description: This script serves as the driver for testing metagenomics analysis.
It calls the necessary functions to simulate reads, perform the pre-processing of the reads, 
coordinating the execution of the pipeline. 
"""

import os
import subprocess

def run_script(script_path, *args):
    # call interpreter explicitly if script isn't executable, otherwise use [script_path] + args
    cmd = f"bash {script_path} {' '.join(str(arg) for arg in args)}"
    subprocess.run(cmd, shell=True, check=True)


# def run_script(script_path):
#     print(f"Running script: {script_path}")
#     exit_code = os.system(f"bash {script_path}")
#     if exit_code != 0:
#         print(f"Error: Script {script_path} failed with exit code {exit_code}.")
#         exit(1)


# scripts_directory = os.getcwd()

scripts_directory = "/home/dolinsek/00_scripts"

# Step 1: Define the paths to the Bash scripts

# Metagenomics:
get_genomes = os.path.join(scripts_directory, "genome_download.sh")
genome_dereplication = os.path.join(scripts_directory, "skder.sh")
genome_checkm = os.path.join(scripts_directory, "checkm_genome.sh")
read_simulation = os.path.join(scripts_directory, "generate_reads.sh")
reads_subsampling = os.path.join(scripts_directory, "subsampling.sh")
assembly_prep = os.path.join(scripts_directory, "assembly_prep.sh")
assembly_prep_subsampled = os.path.join(scripts_directory, "assembly_prep_subsampled.sh")
assembly_metaspades = os.path.join(scripts_directory, "metaspades.sh")
assembly_megahit = os.path.join(scripts_directory, "megahit.sh")
mapping_bowtie2 = os.path.join(scripts_directory, "bowtie2.sh")
binning_coverage = os.path.join(scripts_directory, "coverage.sh")
binning_metabat2 = os.path.join(scripts_directory, "metabat2.sh")
comparison_skani = os.path.join(scripts_directory, "skani.sh")
binning_checkm = os.path.join(scripts_directory, "checkm.sh")
binning_quast = os.path.join(scripts_directory, "quast.sh")
annotation_bakta = os.path.join(scripts_directory, "bakta.sh")
annotation_bakta_genomes = os.path.join(scripts_directory, "bakta_genomes.sh")
annotation_bakta_combined = os.path.join(scripts_directory, "bakta_combined.sh")
annotation_blast = os.path.join(scripts_directory, "blast.sh")
phylogeny_gtdbtk = os.path.join(scripts_directory, "gtdbtk.sh")
phylogeny_gtdbtk_genomes = os.path.join(scripts_directory, "gtdbtk_genomes.sh")

# Metagenomics & Metatranscriptomics:
read_QC = os.path.join(scripts_directory, "fastqc.sh")
read_trimmomatic = os.path.join(scripts_directory, "trimmomatic.sh")
mapping_bbmap = os.path.join(scripts_directory, "bbmap.sh")
reannotation_expert = os.path.join(scripts_directory, "reannotation_expert_operator.sh")
counting_featurecounts = os.path.join(scripts_directory, "featurecounts.sh")
annotation_blast_rrna = os.path.join(scripts_directory, "blast_rrna.sh")
retrive_features = os.path.join(scripts_directory, "get_features.sh")


# Step 1.5: Make sure the carriage return characters in the scripts directory match UNIX format
# grep -IlZ $'\r' -R 00_scripts/ | xargs -0 -r sed -i 's/\r$//'

# Step 2: Execute the Bash scripts sequentially

# sample_names = ["1", "9", "SO4"]
sample_names = ["1"]
# sample_names = ["9", "SO4"]
# assembly_algorithms = ["megahit", "metaspades", "metaspades_single"] 
assembly_algorithms = ["metaspades"] 

threads = 60

# nohup run &
# nohup run > my.log 2>&1 &
# pkill -u dolinsek 
 
# Metagenomic section

for sample_name in sample_names:
    for assembly_algorithm in assembly_algorithms:

        base_directory = f"/home/dolinsek/{sample_name}_mgenomics"
        # reads_directory = f"/home/dolinsek/data/reads_mg/{sample_name}/raw_reads"
        reads_directory = f"/home/dolinsek/data/reads_mg/{sample_name}"
        mtx_directory = f"/home/dolinsek/data/reads_mg/{sample_name}/07_MTX"

        if assembly_algorithm == "megahit":
            assembly_directory = os.path.join(base_directory, "05_assembly_megahit")
        elif assembly_algorithm == "metaspades":
            assembly_directory = os.path.join(base_directory, "06_assembly_metaspades")


        # # Download the genomes
        # run_script(get_genomes, base_directory, sample_name)

        # # Dereplicate the genomes
        # run_script(genome_dereplication, base_directory, threads)

        # Run the checkm bin evaluation script
        # run_script(genome_checkm, base_directory, threads)

        # # Simulate the reads
        # run_script(read_simulation, base_directory)

        # # Run the read quality check script
        # run_script(read_QC, base_directory, reads_directory, threads)

        # # Run the trimmomatic script
        # run_script(read_trimmomatic, reads_directory, threads)

        # # Run the mOTUs classification script
        # run_script(classify_mOTUs)

        # Run the read subsampling script
        # run_script(reads_subsampling, base_directory)

        # Run the read normalization script
        # run_script(reads_normalization, base_directory, threads)

        # Run the metaspades prep script
        # run_script(assembly_prep, reads_directory)

        # Run the metaspades assembly script
        # run_script(assembly_metaspades, base_directory, reads_directory, threads)

        # Run the megahit assembly script
        # run_script(assembly_megahit, base_directory, reads_directory, threads)
     
        # Run the bowtie2 mapping script
        # run_script(mapping_bowtie2, base_directory, assembly_algorithm, reads_directory, threads)

        # Run the coverage info script
        # run_script(binning_coverage, base_directory, assembly_algorithm, threads)

        # Run the metabat2 binning script
        # run_script(binning_metabat2, base_directory, assembly_algorithm, threads)

        # Run the checkm bin evaluation script
        # run_script(binning_checkm, base_directory, assembly_algorithm, threads)

        # Run the quast bin evaluation script
        # run_script(binning_quast, base_directory, assembly_algorithm, threads)

        # Run the skani comparison script
        # run_script(comparison_skani, base_directory, assembly_algorithm, threads)

        # Run the bakta annotation script
        # run_script(annotation_bakta, base_directory, assembly_directory, threads)

        # Run the bakta annotation script
        # run_script(annotation_bakta_genomes, base_directory, threads)

        # Run the bakta annotation script
        # run_script(annotation_bakta_combined, base_directory, assembly_directory, threads)

        # Run the gtdbtk phylogeny assignment script
        # run_script(phylogeny_gtdbtk, base_directory, assembly_algorithm, threads)

        # Run the gtdbtk phylogeny assignment script
        # run_script(phylogeny_gtdbtk_genomes, base_directory, threads)

        # Run the coverm mapping script
        # run_script(mapping_coverm, base_directory, assembly_directory, reads_directory, threads)

        # Run the blast annotation script
        # run_script(annotation_blast, assembly_directory, threads)

        # Run the blast annotation script
        # run_script(reannotation_expert, base_directory, assembly_directory)

        # Run the bbmap mapping script
        # run_script(mapping_bbmap, base_directory, assembly_directory, reads_directory, threads)

        # Run the featureCounts counting script
        # run_script(counting_featurecounts, base_directory, assembly_directory, reads_directory, threads)


# Metatranscriptomics section

for sample_name in sample_names:
    for assembly_algorithm in assembly_algorithms:

        base_directory = f"/home/dolinsek/{sample_name}_mgenomics"
        reads_directory = f"/home/dolinsek/data/Metatranscriptomics/{sample_name}"
        mtx_directory =  f"/home/dolinsek/{sample_name}_mgenomics/07_MTX"

        if assembly_algorithm == "megahit":
            assembly_directory = os.path.join(base_directory, "05_assembly_megahit")
        elif assembly_algorithm == "metaspades":
            assembly_directory = os.path.join(base_directory, "06_assembly_metaspades")
 


        # # Run the read quality check script
        run_script(read_QC, base_directory, reads_directory, threads)

        # # Run the trimmomatic script
        # headcrop = 4
        # run_script(read_trimmomatic, reads_directory, headcrop, threads)

        # Run the bbmap mapping script
        # run_script(mapping_bbmap, base_directory, assembly_directory, reads_directory, threads)

        # Run the featurecounts counting script
        # run_script(counting_featurecounts, base_directory, assembly_directory, reads_directory, threads)

        # Run the blast annotation script
        # run_script(annotation_blast_rrna, mtx_directory, threads)

        # Run the feature retrival script
        # run_script(retrive_features, base_directory)


print("Pipeline execution completed successfully. Maybe...")

