
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


enrichments = ['1_SIE','9_SIM','4_STO']
enrichment_names = ['AT_SIE_01', 'AT_SIM_09', 'DE_STO_04']

enrichment_name_use = dict(zip(enrichments,enrichment_names))

genomes_deseq = dict()


for enrichment in enrichments:
    
    paths = ['C:', 'C:/Users/dolinsekj', 'C:/Users/jando/OneDrive']
    path = 0
    in_deseq_path = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/featurecounts/individual/"
    
    with open(f"{in_deseq_path}genomes_deseq.pkl", "rb") as f:
        genomes_deseq[enrichment] = pickle.load(f)
        

functions = ['cynD','cynS','nit4','nitB','nitC','rhdA']
        
colors = plt.cm.plasma(np.linspace(0, 1, len(functions)))
    
f_colors = dict()

for i, func in enumerate(functions):
    f_colors[func] = colors[int(i)]

to_plot = ['GCA_976997615', 
           'bin_3',
           'bin_5',
           'bin_6',
           'GCA_976996985',
           'GCA_977004765',
           'GCA_977004785',
           'GCA_977004805',]
     


rows=4
columns=2

fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(12, 15), sharex='col', sharey='all')   

# % plotting comparisons

alpha_to_use = 0.4

fig_row = 0
fig_column = 0

j = 0

axes_flat = axes.flatten()

for enrichment, value in genomes_deseq.items():
    
    for genome, value in value.items():
        
        if genome in to_plot:
            
            comparisons = value[0]
            
            keys = list()
            x = list(range(1,len(comparisons)+1))
            
            i = 1
            

            for key, value in comparisons.items():
                
                ax = axes_flat[j]
            
                xs = [i] * (len(value[3]))
                ys = value[3]  
                colors = value[4]
                rank_plot = ax.scatter(    
                    x=xs,
                    y=ys,
                    c=colors, 
                    alpha=alpha_to_use*2,
                    zorder=2,
                    marker="o",
                    s=100,
                )
                
                keys.append(' '.join(key.split('_')[1:5]))
                i += 1
            
                ax.set_ylabel(r"log$_{2}$ fold-change")
                ax.set_title(f'enrichment: {enrichment_name_use[enrichment]}, genome: {genome}')
                     
                
                

            
            
            ax.set_adjustable("datalim")
            
            ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
            ax.set_facecolor('silver')
            
            ax.set_xticks(x,keys,rotation = 30)
            
            

            
            accession = '_'.join(key.split('_')[1:3])
            
            # plt.xlabel(f'DE comparison: {genome_processed}')
            
            plt.tight_layout()
            
            j += 1
            


scatter_legend = ax.legend(

    handles=[
             Line2D([0], [0],
                    color=color, 
                    label=function, 
                    marker="o",
                    markersize=8,
                    alpha = 0.8,
                    linestyle="None",
                    )
             for function, color in f_colors.items()
    ],
    
loc = 'lower center',
title="gene",
ncol=len(functions),
bbox_to_anchor=(-0.065, -0.5),
frameon=True,
facecolor = 'silver'
)

plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/assimilation.png", dpi=600, bbox_inches='tight')
plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/assimilation.svg", bbox_inches='tight')
    


   


