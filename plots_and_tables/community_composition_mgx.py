# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:21:23 2026

@author: jando

https://pydeseq2.readthedocs.io/en/stable/auto_examples/plot_minimal_pydeseq2_pipeline.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html



"""

import pandas as pd
import numpy as np
import os

from Bio import SeqIO


# % Calculate relative abundances from the FeatureCounts data

enrichment = '9_SIM'

# in_fc_file = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/feature_counts/all.txt"
# in_fc_stats = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/feature_counts/all.txt.summary"
# in_fastas = f"C:/Users/jando/OneDrive/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/genomes/genomes/"

in_fc_file = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/feature_counts_all/all.txt"
in_fc_stats = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/feature_counts_all/all.txt.summary"
in_fastas = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/genomes/genomes_cleaned/"
 
folder_figures = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/Figures and tables/"
read_length = 2 * 146

for files_tmp in os.walk(in_fastas):
     fastas = [in_fastas + file for file in files_tmp[2]]

headers = dict()
genomes = []

for fasta in fastas:
    genome = fasta.split('/')[-1].removesuffix('.fna')
    genomes.append(genome)
    for seq_record in SeqIO.parse(fasta, "fasta"):
        headers[seq_record.id] = genome
        
counts = pd.read_table(in_fc_file, header=1)

contigs_fc = set(counts['Chr'])
contigs_headers = set([key for key, value in headers.items()])

cols = list(counts.columns)
cols_new = [name.split('/')[-1] for name in cols]
samples = [name.split('/')[-1] for name in cols if '/' in name]
counts.columns = cols_new
counts['Genome'] = counts['Chr'].apply(lambda x: headers[x])



genomes_stats_fc = pd.DataFrame({'Genome': genomes})

for sample in samples:
    genome_sums = counts.groupby('Genome')[sample].sum()
    genomes_stats_fc[sample] = genomes_stats_fc['Genome'].map(genome_sums)

genome_len = counts.groupby('Genome')['Length'].sum()
genomes_stats_fc['Length'] = genomes_stats_fc['Genome'].map(genome_len)


for sample in samples:
    genomes_stats_fc[sample + '_depth'] = genomes_stats_fc[sample] * read_length / genomes_stats_fc['Length']

for sample in samples:
    genomes_stats_fc[sample + '_relative'] = 100 * genomes_stats_fc[sample + '_depth'] / genomes_stats_fc[sample + '_depth'].sum()


genomes_stats_fc_new = genomes_stats_fc.set_index('Genome')
genomes_stats_fc_rel = genomes_stats_fc_new[[col for col in genomes_stats_fc_new.columns if 'relative' in col]]
cols_plot = genomes_stats_fc_rel.columns
sort = genomes_stats_fc_rel.columns[0]
genomes_stats_fc_rel_sorted = genomes_stats_fc_rel.sort_values(by=sort)
genomes_stats_fc_rel_sorted = genomes_stats_fc_rel_sorted[[cols_plot[3],cols_plot[0],cols_plot[1],cols_plot[2]]]
        
genomes_stats_fc_rel_sorted.to_excel(folder_figures + f'{enrichment}_relative_mgx.xlsx', sheet_name="Relative abundances MGX")
    
# % Calculate read assignmet stats from the Samtools coverage summary data

genomes_stats_st = pd.DataFrame()   

for sample in samples: 
    
    # in_samtools_stats = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/feature_counts_all/{sample}_contig_coverage.tsv"
    in_samtools_stats = f"C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/feature_counts_all/{sample}_contig_coverage.tsv"

    sts = pd.read_table(in_samtools_stats)
    sts['Genome'] = sts['#rname'].apply(lambda x: headers[x])
        
    genome_len = sts.groupby('Genome')['endpos'].sum()
    sts['Length'] = sts['Genome'].map(genome_len)
    sts['meandepth_adj'] = sts['meandepth'] * sts['endpos'] / sts['Length']
    genomes_stats_st[sample] = sts.groupby('Genome')['meandepth_adj'].sum()
    # genomes_stats_st = genomes_stats_st.to_frame()
    genomes_stats_st[sample + '_relative'] = 100  * genomes_stats_st[sample]/genomes_stats_st[sample].sum()


genomes_stats_st_rel = genomes_stats_st[[col for col in genomes_stats_st.columns if 'relative' in col]]
cols_plot = genomes_stats_st_rel.columns
sort = genomes_stats_st_rel.columns[0]
genomes_stats_st_rel_sorted = genomes_stats_st_rel.sort_values(by=sort)
genomes_stats_st_rel_sorted = genomes_stats_st_rel_sorted[[cols_plot[3],cols_plot[0],cols_plot[1],cols_plot[2]]]


# % Calculate read assignmet stats from the FeatureCounts summary data

counts_stats = pd.read_table(in_fc_stats, index_col=0)
cols_stats = list(counts_stats.columns)
cols_stats_new = [name.split('/')[-1] for name in cols_stats]
counts_stats.columns = cols_stats_new

for sample in samples:
    counts_stats[sample + '_relative'] = 100 * counts_stats[sample] / counts_stats[sample].sum()
  
counts_stats_rel = counts_stats[[col for col in counts_stats.columns if 'relative' in col]]

counts_stats_agg = pd.DataFrame()   
counts_stats_agg['mean'] = counts_stats_rel.mean(axis=1)
counts_stats_agg['std'] = counts_stats_rel.std(axis=1)



# %% Plotting: 3 columns, stacked logy for community composition, 1 row for featurecounts, one for Samtools 


import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

times = [0,7,22,46]
rows=2
fig_cols=2

fig, axes = plt.subplots(nrows=rows, ncols=fig_cols, figsize=(6, 8), sharey='row', sharex='col', gridspec_kw={'width_ratios': [3, 1]})   

num_colors = len(genomes)
colors = plt.cm.plasma(np.linspace(0.8, 0, num_colors))      

row = 0
fig_cols = 0


genome_names = list(genomes_stats_st_rel_sorted.index)
legend = []
for genome in genome_names:
    legend.append(genome.split('.1_')[0])
        
ax = axes[row, fig_cols]
ax.stackplot(times, genomes_stats_st_rel_sorted, colors=colors)
ax.set_title(r'$\it{Samtools}$ coverage estimate')
ax.set_xlim(left=0, right=46)
ax.set_xticks(times)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')
ax.legend(legend, title="genomes & MAGs", loc= 'center right', bbox_to_anchor=(1.62, -0.1))

row = 1
fig_cols = 0

   
ax = axes[row, fig_cols]
ax.stackplot(times, genomes_stats_fc_rel_sorted, colors=colors)
ax.set_title(r'$\it{FeatureCounts}$ coverage estimate')
ax.set_xlabel('Time (hours)', fontsize=12)
ax.set_ylabel('Relative Abundance (%)', y=1.1, fontsize=12)
ax.set_xlim(left=0, right=46)
ax.set_xticks(times)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

axes[0, 1].axis('off')
axes[1, 1].axis('off')



# Save the figure to a file instead of displaying
output_file = os.path.join(folder_figures, f'relative_abundance_mgx_{enrichment}.png')
plt.savefig(output_file, dpi=600, bbox_inches='tight')

output_file = os.path.join(folder_figures, f'relative_abundance_mgx_{enrichment}.svg')
plt.savefig(output_file, format='svg', bbox_inches='tight')   










# %%



