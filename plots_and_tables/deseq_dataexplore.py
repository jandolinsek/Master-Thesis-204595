
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


enrichments = ['1_SIE','9_SIM','4_STO']
enrichment_names = ['AT_SIE_01', 'AT_SIM_09', 'DE_STO_04']

panels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

enrichment_name_use = dict(zip(enrichments,enrichment_names))

genomes_deseq = dict()


for enrichment in enrichments:
    
    paths = ['C:', 'C:/Users/dolinsekj', 'C:/Users/jando/OneDrive']
    path = 1
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

comparisons = ['dds_all_CN_vs_NH4_resLFC_apeglm',
               'dds_CN_adapt_vs_exp_resLFC_apeglm',
               'dds_CN_adapt_vs_stat_resLFC_apeglm',
               'dds_CN_exp_vs_stat_resLFC_apeglm',
               'dds_exp_CN_vs_NH4_resLFC_apeglm',       
               'dds_stat_CN_vs_NH4_resLFC_apeglm']

# %% target genes plot

rows=4
columns=2

fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(12, 15), sharex='col', sharey='all')   

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

# plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/assimilation.png", dpi=600, bbox_inches='tight')
# plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/assimilation.svg", bbox_inches='tight')
    
# %% volcano plots

for comparison in comparisons:

    rows=4
    columns=2
    
    fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(12.5, 15)) 
    alpha_to_use = 0.4
    
    fig_row = 0
    fig_column = 0

    j = 0
    
    axes_flat = axes.flatten()
    
    for enrichment, value in genomes_deseq.items():
        
        for genome, value in value.items():
            
            if genome in to_plot:
                
                dds = value[1][comparison][0]
                
                padj_thresh = 0.05
                log2fc_thresh_up = np.log(4)
                log2fc_thresh_down = -np.log(4)
    
                padjs = dds["padj"].apply(lambda x: True if x < padj_thresh else False)
                log2fcs = dds["log2FoldChange"].apply(lambda x: True if x < log2fc_thresh_down or x > log2fc_thresh_up else False)
                combined = padjs & log2fcs
                combined_reverse = ~combined
    
                colors = combined.apply(lambda x: 'darkred' if x == True else 'dimgray')
                 
                significant_up = dds[dds["padj"] < padj_thresh]
                significant_up = significant_up[significant_up["log2FoldChange"] > log2fc_thresh_up]
                significant_down = dds[dds["padj"] < padj_thresh]
                significant_down = significant_down[significant_down["log2FoldChange"] < log2fc_thresh_down]
                notsignificant = dds[combined_reverse]
                
                ax = axes_flat[j]
                
                Volcano_plot = ax.scatter(    
                    x=significant_up["log2FoldChange"],
                    y=significant_up["padjs_transformed"],
                    c='darkred', 
                    alpha=alpha_to_use,
                    zorder=5,
                )
                
                Volcano_plot = ax.scatter(    
                    x=significant_down["log2FoldChange"],
                    y=significant_down["padjs_transformed"],
                    c='navy', 
                    alpha=alpha_to_use,
                    zorder=5,
                )
                
                Volcano_plot = ax.scatter(    
                    x=notsignificant["log2FoldChange"],
                    y=notsignificant["padjs_transformed"],
                    c='dimgray', 
                    alpha=alpha_to_use,
                    zorder=2,
                )
                
                ax.set_adjustable("datalim")
                
                ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
                ax.set_facecolor('silver')
                
                ax.set_xlabel(r"log$_{2}$ fold change")
                ax.set_ylabel(r"-log$_{10}$(p$_{adj}$)")
                ax.set_title(f'enrichment: {enrichment_name_use[enrichment]}, genome: {genome}')
                
                plt.tight_layout()
                
                j += 1
                
    ax.legend(['significant upregulated (4x)', 'significant downregulated (4x)', 'not regulated'],
              loc = 'lower center',
              title="gene regulation",
              ncol=3,
              bbox_to_anchor=(-0.065, -0.4),  
              facecolor = 'silver'
              )
        
    
    # plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{comparison}_volcano_plots.png", dpi=300, bbox_inches='tight')
    # plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{comparison}_volcano_plots.svg", bbox_inches='tight')
        

# %% MA plots

for comparison in comparisons:
    
    rows=4
    columns=2
    
    fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(12.5, 15))   
    
    alpha_to_use = 0.4
    
    fig_row = 0
    fig_column = 0
    
    j = 0
    
    axes_flat = axes.flatten()
    
    for enrichment, value in genomes_deseq.items():
        
        for genome, value in value.items():
            
            if genome in to_plot:
                
                dds = value[1][comparison][0]
                
                colormap = plt.cm.plasma
                
                padj_thresh = 0.05
                padjs_transformed = dds["padj"].apply(lambda x: -np.log10(x))
                
                dds["padjs_transformed"] = dds["padj"].apply(lambda x: -np.log10(x))
                
                ax = axes_flat[j]
    
                significant = dds[dds["padj"] < padj_thresh]
                notsignificant = dds[dds["padj"] >= padj_thresh]
                
                MAplot = ax.scatter(    
                    x=notsignificant["baseMean"],
                    y=notsignificant["log2FoldChange"],
                    c='dimgray', 
                    alpha=alpha_to_use,
                    zorder=2,
                )
                
                MAplot = ax.scatter(    
                    x=significant["baseMean"],
                    y=significant["log2FoldChange"],
                    c=significant["padjs_transformed"], 
                    alpha=alpha_to_use,
                    zorder=3,
                    
                )
                
                ax.set_adjustable("datalim")
                
                ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
                ax.set_facecolor('silver')
                ax.set_title(f'enrichment: {enrichment_name_use[enrichment]}, genome: {genome}')
    
                ax.set_xlabel("mean of normalized counts")
                ax.set_ylabel(r"log$_{2}$ fold change")
                
                log = True 
                
                if log is True:
                    ax.set_xscale("log")
                
                cbar = fig.colorbar(MAplot, ax=ax, pad=0.03)
                cbar.set_label("$-\log_{10}(\\text{p}_{\\text{adj}})$", fontsize=12)
                
                plt.tight_layout()
                    
                j += 1
    
    
    # plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{comparison}_MA_plots.png", dpi=600, bbox_inches='tight')
    # plt.savefig(f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{comparison}_MA_plots.svg", bbox_inches='tight')
    

# %%

to_plot = ['GCA_976997615', 
           # 'bin_3',
           # 'bin_5',
           # 'bin_6',
           # 'GCA_976996985',
           # 'GCA_977004765',
           # 'GCA_977004785',
           # 'GCA_977004805',
           ]


padj_thresh = 0.05
regulation_factor = 2
log2fc_thresh_up = np.log(regulation_factor)
log2fc_thresh_down = -np.log(regulation_factor)
        
        
rows=3
columns=2

fig, axes = plt.subplots(nrows=rows, 
                         ncols=columns, 
                         figsize=(12, 15), 
                         sharex='col', 
                         sharey='all',
                         layout="constrained",
                         )   

alpha_to_use = 0.4

fig_row = 0
fig_column = 0

j = 0

axes_flat = axes.flatten()

for enrichment, value in genomes_deseq.items():
    
    for genome, value in value.items():
        
        if genome in to_plot:
            
            
            organism = genome
            enrich = enrichment
            
            for comparison in comparisons:
            
                dds = value[1][comparison][0]
                
                significant = dds[dds['padj'] < padj_thresh]
                significant_upregulated = significant[significant["log2FoldChange"] > log2fc_thresh_up]
                significant_downregulated = significant[significant["log2FoldChange"] < log2fc_thresh_down]
             
                ax = axes_flat[j]
                
                rank_plot = ax.scatter(    
                    x=dds["gene_rank"],
                    y=dds["log2FoldChange"],
                    c='gray', 
                    alpha=alpha_to_use/4,
                    zorder=1,
                )
                
                rank_plot = ax.scatter(    
                    x=significant_upregulated["gene_rank"],
                    y=significant_upregulated["log2FoldChange"],
                    c='darkred', 
                    alpha=alpha_to_use/2,
                    zorder=5,
                )
                
                rank_plot = ax.scatter(    
                    x=significant_downregulated["gene_rank"],
                    y=significant_downregulated["log2FoldChange"],
                    c='navy', 
                    alpha=alpha_to_use/2,
                    zorder=5,
                )
                
                ax.set_yticks(list(range(-8,12,2)))
                ax.set_ylim([-8,10])
            
                yticks = [-8,10]
            
                ax.vlines(x=value[1][comparison][1]['assimilation']['gene_rank_x'], 
                          ymin=min(yticks), ymax=max(yticks), color=colors[1], 
                          linestyle='-', lw=3, alpha=0.1)
                
                ax.vlines(x=value[1][comparison][1]['adaptation']['gene_rank_x'], 
                          ymin=min(yticks), ymax=max(yticks), color=colors[-2], 
                          linestyle='-', lw=3, alpha=0.1)
            
                ax.set_adjustable("datalim")
                
                ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
                ax.set_facecolor('lightgray')
                ax.set_title(comparison)
            
                # ax.text(x, y, panel[j])
                ax.text(6400, 8.5,
                        panels[j],
                        fontsize='xx-large',
                        # verticalalignment='top', 
                        # horizontalalignment='right',
                        )
            
            # verticalalignment
                
                scatter_legend = ax.legend(
                    handles=[
                        Line2D(
                            [0], [0],
                            marker="o",
                            linestyle="None",
                            color="darkred",
                            label="upregulated",
                            markersize=8,
                            alpha = 0.5,
                        ),
                        
                        Line2D(
                            [0], [0],
                            marker="o",
                            linestyle="None",
                            color="navy",
                            label="downregulated",
                            markersize=8,
                            alpha = 0.5,
                        ),
                        
                        Line2D(
                            [0], [0],
                            marker="o",
                            linestyle="None",
                            color="dimgray",
                            label="not regulated",
                            markersize=8,
                            alpha = 0.5,
                        )
                    ],
                    # title="Regulation",
                    # bbox_to_anchor=(1.02, 0.2),
                    loc="lower left",
                    frameon=True,
                    facecolor='silver',
            
                )
                
                ax.add_artist(scatter_legend)
            
            
                vlines_legend = ax.legend(
                    handles=[
                        Line2D(
                            [0], [0],
                            # marker="-",
                            linewidth=3,
                            color=colors[1],
                            label="top assimilation",
                            markersize=8,
                            alpha = 1,
                        ),
                        
                        Line2D(
                            [0], [0],
                            # marker="o",
                            linewidth=3,
                            color=colors[-2],
                            label="top adaptation",
                            markersize=8,
                            alpha = 1,
                        ),
                        
                    ],
                    # title="Regulation",
                    # bbox_to_anchor=(1.02, 0.2),
                    loc="upper left",
                    frameon=True,
                    facecolor='silver',
                )
                
                
                log = False 
                
                if log is True:
                    plt.xscale("log")
                

                plt.tight_layout()
                
                if j == 2:
                
                    ax.set_ylabel(r"log$_{2}$ fold change", fontsize=12)

                j += 1
                
                
                
            # plt.xlabel(r"genome position (gene number)", fontsize=12)
            # plt.xlabel(" ", fontsize=12)
            
fig.supxlabel(r"genome position (gene number)", 
              fontsize=12, 
              x=0.52,
              y=-0.01,
              )

in_deseq_path = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrich}/featurecounts/individual/"
  
# plt.savefig(f'{in_deseq_path}{organism}_all_v2.png', dpi=300, bbox_inches='tight')
# plt.savefig(f'{in_deseq_path}{organism}_all_v2.svg', bbox_inches='tight')
      

# %%

start = 3931
end = 3970

for enrichment, value in genomes_deseq.items():
    
    for genome, value in value.items():
        
        if genome in to_plot:
            
            
            organism = genome
            enrich = enrichment
            
            for comparison in comparisons:
            
                dds = value[2][comparison]


                print('Comparison: ', comparison)
                print('Organism: ', organism)
                print(f'start: {start}   end: {end}')
                print('mean L2FC: ', dds["log2FoldChange"].iloc[start:end].mean())
                print('std L2FC: ', dds["log2FoldChange"].iloc[start:end].std())
                print('mean padj: ', dds["padj"].iloc[start:end].mean())
                print('std padj: ', dds["padj"].iloc[start:end].std())