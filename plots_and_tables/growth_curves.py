# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:12:06 2026

@author: AI & jando 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import os

folder_data = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/Metadata/"
folder_figures = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/Figures/"

file = folder_data + "DNA_RNA_CN_extracts.xlsx"

data = pd.read_excel(file)
results = dict()

# 1. Sort the DataFrame hierarchically
sorted_data = data.sort_values(
    by=['Sample', 'Nitrogen', 'Replicate'], 
    ascending=[True, True, True]  # Optional: control direction for each column
)

data['log DNA'] = np.log10(data['DNA'])

# Now you can easily calculate the mean across replicates for each sample/condition:

summary_CN = data.groupby(['Sample', 'Nitrogen','Time'])['Cyanide mM'].agg(['mean', 'std', list]).reset_index()
summary_CN.rename(columns={'list': 'Replicates'}, inplace=True)    
    
summary_DNA = data.groupby(['Sample', 'Nitrogen','Time'])['DNA'].agg(['mean', 'std', list]).reset_index()
summary_DNA.rename(columns={'list': 'Replicates'}, inplace=True)

summary_DNA_log = data.groupby(['Sample', 'Nitrogen','Time'])['log DNA'].agg(['mean', 'std', list]).reset_index()
summary_DNA_log.rename(columns={'list': 'Replicates'}, inplace=True)

growth_stage = data.groupby(['Sample', 'Nitrogen','Time'])['RNA/DNA'].agg(['mean', 'std', list]).reset_index()
growth_stage.rename(columns={'list': 'Replicates'}, inplace=True)

samples = list(set(summary_DNA['Sample']))
nitrogens = list(set(summary_DNA['Nitrogen']))
                 

rows=3
columns=3

fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(10, 8), sharey='row', sharex='col')   

num_colors = 10
color_10 = plt.cm.plasma(np.linspace(0, 1, num_colors))      


# Plotting CN values

row = 0

for i, sample in enumerate(samples):
    
    legend = []
    
    for nitrogen in nitrogens:
        
        part_sample = summary_CN[summary_CN['Sample'] == sample]
        part_sample_nitrogen = part_sample[part_sample['Nitrogen'] == nitrogen]
        
        if nitrogen == 'CN-':
            color = color_10[5]
            legend.append(Line2D([0], [0], color=color, lw=2, label=nitrogen))
        else:
            color = color_10[0]
            legend.append(Line2D([0], [0], color=color, lw=2, label=nitrogen))
            
        ax = axes[row, i]
        
        ax.plot(part_sample_nitrogen['Time'], part_sample_nitrogen['mean'], color=color, lw=2)
        ax.fill_between(part_sample_nitrogen['Time'],
                        part_sample_nitrogen['mean'] - part_sample_nitrogen['std'], 
                        part_sample_nitrogen['mean'] + part_sample_nitrogen['std'], 
                        color=color, alpha=0.2, label='± 1 SD')

        # ax.set_xlabel('Time (hours)')
        ax.set_xticklabels([])
        ax.grid(True, alpha=0.3)
        ax.set_title(f'{sample}')
        ax.set_facecolor('whitesmoke')
        ax.legend(handles=legend, title="Nitrogen Source")

        
axes[0,0].set_ylabel('Cyanide (mM)')

        

# Plotting DNA values

row = 1

for i, sample in enumerate(samples):
    
    legend = []
    
    for nitrogen in nitrogens:
        
        part_sample = summary_DNA[summary_DNA['Sample'] == sample]
        part_sample_nitrogen = part_sample[part_sample['Nitrogen'] == nitrogen]
        
        if nitrogen == 'CN-':
            color = color_10[5]
            legend.append(Line2D([0], [0], color=color, lw=2, label=nitrogen))
        else:
            color = color_10[0]
            legend.append(Line2D([0], [0], color=color, lw=2, label=nitrogen))
            
        ax = axes[row, i]
        
        ax.plot(part_sample_nitrogen['Time'], part_sample_nitrogen['mean'], color=color, lw=2)
        ax.fill_between(part_sample_nitrogen['Time'],
                        part_sample_nitrogen['mean'] - part_sample_nitrogen['std'], 
                        part_sample_nitrogen['mean'] + part_sample_nitrogen['std'], 
                        color=color, alpha=0.2, label='± 1 SD')

        # ax.set_xlabel('Time (hours)')
        ax.set_xticklabels([])
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        # ax.set_title(f'{sample}')
        ax.set_facecolor('whitesmoke')
        # ax.legend(handles=legend, title="Nitrogen Source")

        
axes[1,0].set_ylabel('DNA (ng / mL culture)')

        
# Plotting RNA/DNA ratio

row = 2

for i, sample in enumerate(samples): 
    
    legend = []
    
    for nitrogen in nitrogens:

        part_sample = growth_stage[growth_stage['Sample'] == sample]
        part_sample_nitrogen = part_sample[part_sample['Nitrogen'] == nitrogen]
        
        if nitrogen == 'CN-':
            color = color_10[5]
            legend.append(Line2D([0], [0], color=color, lw=2, label=nitrogen))
        else:
            color = color_10[0]
            legend.append(Line2D([0], [0], color=color, lw=2, label=nitrogen))
            
        ax = axes[row, i]
       
        ax.plot(part_sample_nitrogen['Time'], part_sample_nitrogen['mean'], color=color, lw=2)
        ax.fill_between(part_sample_nitrogen['Time'],
                        part_sample_nitrogen['mean'] - part_sample_nitrogen['std'], 
                        part_sample_nitrogen['mean'] + part_sample_nitrogen['std'], 
                        color=color, alpha=0.2, label='± 1 SD')

        ax.set_xlabel('Time (hours)')
        ax.grid(True, alpha=0.3)
        # ax.set_title(f'{sample}')
        # ax.legend(handles=legend, title="Nitrogen")
        ax.set_facecolor('whitesmoke')
        ax.set_xticklabels([0,0,20,40,60,80,100])

      
           
axes[2,0].set_ylabel('RNA/DNA')


        
plt.tight_layout()
# plt.show()
        
# Save the figure to a file instead of displaying
output_file = os.path.join(folder_figures, 'CN_DNA_and_RNA_DNA_ratios.png')
plt.savefig(output_file, dpi=600, bbox_inches='tight')

output_file = os.path.join(folder_figures, 'CN_DNA_and_RNA_DNA_ratios.svg')
plt.savefig(output_file, format='svg', bbox_inches='tight')   