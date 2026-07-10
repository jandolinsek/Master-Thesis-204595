# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:48:45 2026

@author: jando & AI
"""


import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

enrichments = ['1_SIE','9_SIM','4_STO']
enrichment_names = ['AT_SIE_01', 'AT_SIM_09', 'DE_STO_04']
enrichment_name_use = dict(zip(enrichments,enrichment_names))


rows=3
columns=1

fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(8, 10), sharex='col')   

fig_row = 0
fig_column = 0


for enrichment in enrichments:
# enrichment = enrichments[2]

    paths = ['C:', 'C:/Users/dolinsekj', 'C:/Users/jando/OneDrive']
    path = 0
    in_skani_file = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/{enrichment}/results_skani_tab.tsv"
        
    # skani_results = pd.read_table(in_skani_file, delimiter='\t')
    skani_results = pd.read_table(in_skani_file, delimiter='\t', usecols=['ANI'])
    
    ax = axes[fig_row]
    
    ax.hist(skani_results['ANI'], bins=100, color='dimgray', edgecolor='black', alpha=0.7)
    
    if fig_row > 1:
        ax.set_xlabel('ANI (%)', fontsize=12)
    
    ax.set_ylabel('Pairwise counts', fontsize=12)
    ax.set_title(f'Pairwise ANI, enrichment: {enrichment_name_use[enrichment]}', fontsize=12)
    
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    ax.axvline(x=99.0, color='blue', linestyle='--', linewidth=1.5, label='Merge cutoff (99% ANI)')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()

    fig_row += 1


plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/ANI_all.png", dpi=600, bbox_inches='tight')
plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/ANI_all.svg", bbox_inches='tight')
    

