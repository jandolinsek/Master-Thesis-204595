# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:42:50 2026

@author: DolinsekJ
"""


import pandas as pd
import numpy as np

import os
from os.path import join

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# % Calculate relative abundances from the FeatureCounts data

enrichment = '1_SIE'

paths = ['C:', 'C:/Users/dolinsekj', 'C:/Users/jando/OneDrive']
path = 0
in_deseq_file = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/featurecounts/counts_GCA_976997615.tsvdds_exponential_CN_vs_NH4_resLFC_apeglm.csv"
in_deseq_path = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/featurecounts/individual/"
in_fastas = f"{paths[path]}/Master Thesis Share/{enrichment}/genomes/" 
in_metadata = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/featurecounts/design_table.tsv"
folder_figures = "{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/Figures and tables/"
in_MAGs_genomes = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/MAGs_genomes_of_interest.txt"
in_blast = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/featurecounts/combined_features_blast.tsv"
in_excel = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/01_metadata/CYA_degradation_genes_JD.xlsx"
in_excel_assimilation = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/01_metadata/CYA_degradation_genes_JD_assimilation.xlsx"
in_excel_assimilation_strict = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/01_metadata/CYA_degradation_genes_JD_assimilation_strict.xlsx"

# significant_upregulated_top_assimilation = pd.read_excel(in_deseq_path + 'top50_assimilation.xlsx') 
# significant_upregulated_top_adaptation = pd.read_excel(in_deseq_path + 'top50_adaptation.xlsx')


dirs_tmp = os.listdir(in_deseq_path)
dirs_tmp = [in_deseq_path + dir_tmp + '/' for dir_tmp in dirs_tmp]


for dir_tmp in dirs_tmp:
    
    
    
    files_tmp = os.listdir(dir_tmp)
    
    if 'GCA_' in dir_tmp:
        genome_processed = dir_tmp.split('_')[-2] + '_' + dir_tmp.split('_')[-1].split('.')[0] # use for genomes
        print(genome_processed)
    elif 'bin.' in dir_tmp:
        genome_processed = dir_tmp.split('_')[-1].split('.')[0] + '_' + dir_tmp.split('_')[-1].split('.')[1] # use for bins
        print(genome_processed)


    MAGs_genomes_df = pd.read_table(in_MAGs_genomes, header=None, names=['genome'])
    MAGs_genomes = set(MAGs_genomes_df['genome'])
    
    in_annotations = f"{paths[path]}/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MTX/{enrichment}/featurecounts/combined_features.tsv"
    annotations_headers = ['SequenceId', 'Type', 'Start', 'Stop', 'Strand_Locus', 'Geneid',	'Gene', 'Product', 'DbXrefs']
    
    blast_headers = ['qseqid', 'sseqid', 'pident', 'qcovs', 'length', 'qlen', 'slen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
    blast_results = pd.read_table(in_blast, names=blast_headers)
    
    blast_info = pd.read_excel(in_excel_assimilation_strict)
    blast_info['sseqid'] = blast_info['protein_id'] + '|' + blast_info['entry_name']
    
    
    genes_of_interest_significant = dict()
    
    functions_list = sorted(list(set(blast_info['function'])))
    
    functions = dict()
    i = 0
    
    for function in functions_list:
        functions[function] = i
        i +=1
    
    
    files_dds = [dir_tmp + file for file in files_tmp if "dds" in file]
    files_dds = [file for file in files_dds if '.png' not in file]
    files_dds = [file for file in files_dds if '.svg' not in file]
  


    # % plotting comparisons
    
    alpha_to_use = 0.4
    
    padj_thresh = 0.05
    regulation_factor = 2
    log2fc_thresh_up = np.log(regulation_factor)
    log2fc_thresh_down = -np.log(regulation_factor)
    
    for file_dds in files_dds:
        
        if "exp_CN_vs_NH4" in file_dds:
         
            dds_rank = pd.read_table(file_dds, sep=',', header=0, index_col=0)
            dds_rank['gene_number'] = dds_rank.index
            dds_rank['gene_rank'] = dds_rank['gene_number'].apply(lambda x: int(x.split('_')[1]))
            
            significant = dds_rank[dds_rank["padj"] < padj_thresh]
            significant_upregulated = significant[significant["log2FoldChange"] > log2fc_thresh_up]
            significant_downregulated = significant[significant["log2FoldChange"] < log2fc_thresh_down]
        
            significant_upregulated_assimilation_top20 = significant_upregulated.sort_values(by='log2FoldChange', ascending=False).head(20)
            significant_upregulated_assimilation_top50 = significant_upregulated.sort_values(by='log2FoldChange', ascending=False).head(50)
    
        elif "CN_adapt_vs_exp" in file_dds:
            
            
            dds_rank = pd.read_table(file_dds, sep=',', header=0, index_col=0)
            dds_rank['gene_number'] = dds_rank.index
            dds_rank['gene_rank'] = dds_rank['gene_number'].apply(lambda x: int(x.split('_')[1]))
            
            significant = dds_rank[dds_rank["padj"] < padj_thresh]
            significant_upregulated = significant[significant["log2FoldChange"] > log2fc_thresh_up]
            significant_downregulated = significant[significant["log2FoldChange"] < log2fc_thresh_down]
        
            significant_upregulated_adaptation_top20 = significant_upregulated.sort_values(by='log2FoldChange', ascending=False).head(20)
            significant_upregulated_adaptation_top50 = significant_upregulated.sort_values(by='log2FoldChange', ascending=False).head(50)
    
    
    
    # files_dds = [file for file in files_dds if "exp_vs_stat" in file]

# %


    rows=6
    columns=1

    fig, axes = plt.subplots(nrows=rows, ncols=columns, figsize=(11, 15), sharex='col')   
    
    # % plotting comparisons
    
    alpha_to_use = 0.4
    
    fig_row = 0
    
    for file_dds in files_dds:
        
        processing = file_dds.split('/')[-1].replace('.tsv','_').replace('.csv','').replace('counts_','')
    
        dds = pd.read_table(file_dds, sep=',', header=0, index_col=0)
        dds.index.name = "Geneid"
        metadata = pd.read_table(in_metadata)
        
        dds['gene_rank'] = list(range(1,len(dds)+1))
        dds['gene_number'] = dds.index
        dds['gene_rank'] = dds['gene_number'].apply(lambda x: int(x.split('_')[1]))
            
       
    
        blast_annotated = pd.merge(blast_info, blast_results, on="sseqid", how="inner")
        blast_annotated.rename(columns={"qseqid": "Geneid"}, inplace=True)
        
        annotations = pd.read_table(in_annotations, names=annotations_headers)
        annotations = annotations.set_index('Geneid')
        
        # % protein tables
        
        
    
        
        padjs = dds["padj"].apply(lambda x: True if x < padj_thresh else False)
        log2fcs_up = dds["log2FoldChange"].apply(lambda x: True if x > log2fc_thresh_up else False)
        combined_up = padjs & log2fcs_up
        upregulated = dds[combined_up]
        
        padjs = dds["padj"].apply(lambda x: True if x < padj_thresh else False)
        log2fcs_down = dds["log2FoldChange"].apply(lambda x: True if x < log2fc_thresh_down else False)
        combined_down = padjs & log2fcs_down
        downregulated = dds[combined_down]
        
        all_annotated_expert = pd.merge(dds, blast_annotated, on="Geneid", how="inner")
        all_annotated = pd.merge(dds, annotations, on="Geneid", how="inner")
        
        upregulated_annotated = pd.merge(upregulated, annotations, on="Geneid", how="inner")
        downregulated_annotated = pd.merge(downregulated, annotations, on="Geneid", how="inner")
        
        upregulated_annotated_expert = pd.merge(upregulated_annotated, blast_annotated, on="Geneid", how="inner")
        downregulated_annotated_expert = pd.merge(downregulated_annotated, blast_annotated, on="Geneid", how="inner")
        
        dds["padjs_transformed"] = dds["padj"].apply(lambda x: -np.log10(x))
        
    
        
        dds_sorted = dds.sort_values(by='log2FoldChange', ascending=False)
        dds_sorted['rank'] = list(range(1,len(dds_sorted)+1))
        
        blast_Geneids = set(all_annotated_expert['Geneid'])
        
        all_annotated_expert_merged = pd.merge(dds_sorted, blast_annotated, on="Geneid", how="left")
        
        all_annotated_expert_merged_best = (
            all_annotated_expert_merged.sort_values("pident", ascending=False)
              .drop_duplicates(subset="Geneid", keep="first")
        )
        
        genes_of_interest = all_annotated_expert_merged_best["pident"].notna()
        
        all_annotated_expert_merged_best['genes_of_interest'] = genes_of_interest
        all_annotated_expert_merged_best['log2FoldChange_goi'] = all_annotated_expert_merged_best['log2FoldChange'] * all_annotated_expert_merged_best['genes_of_interest']
        all_annotated_expert_merged_best['log2FoldChange_goi'] = all_annotated_expert_merged_best['log2FoldChange'] * all_annotated_expert_merged_best['genes_of_interest']
        all_annotated_expert_merged_best["log2FoldChange_bar"] = all_annotated_expert_merged_best["log2FoldChange"].apply(lambda x: x if x < padj_thresh else 0)
    
        
        significant = all_annotated_expert_merged_best[all_annotated_expert_merged_best["padj"] < padj_thresh]
        significant_upregulated = significant[significant["log2FoldChange"] > log2fc_thresh_up]
        significant_downregulated = significant[significant["log2FoldChange"] < log2fc_thresh_down]
            
        colors = plt.cm.plasma(np.linspace(0, 1, len(functions)))
            
        f_colors = dict()
        
        for func, i in functions.items():
            f_colors[func] = colors[int(i)]
            
        all_annotated_expert_merged_best["f_color"] = (
            all_annotated_expert_merged_best["function"]
            .map(f_colors)
            .fillna("lightgray"))
    
        all_annotated_expert_merged_best_box = all_annotated_expert_merged_best[all_annotated_expert_merged_best['padj'] < padj_thresh]
        significant_expert_bool=all_annotated_expert_merged_best_box["pident"].notna()
        significant_expert=all_annotated_expert_merged_best_box[significant_expert_bool]
        genes_of_interest_significant[processing] = [list(significant_expert['Geneid']),
                                                     list(significant_expert['gene_cur']),
                                                     list(significant_expert['function']),
                                                     list(significant_expert['log2FoldChange']),
                                                     list(significant_expert['f_color'])]
         
        
        # # % volcano plot
        
        # padj_thresh = 0.05
        # log2fc_thresh_up = np.log(2)
        # log2fc_thresh_down = -np.log(2)
        
        # padjs = dds["padj"].apply(lambda x: True if x < padj_thresh else False)
        # log2fcs = dds["log2FoldChange"].apply(lambda x: True if x < log2fc_thresh_down or x > log2fc_thresh_up else False)
        # combined = padjs & log2fcs
        
        # colors = combined.apply(lambda x: 'darkred' if x == True else 'dimgray')
        
        # fig, ax = plt.subplots()
        
        # significant_up = dds[dds["padj"] < padj_thresh]
        # significant_up = significant_up[significant_up["log2FoldChange"] > log2fc_thresh_up]
        # significant_down = dds[dds["padj"] < padj_thresh]
        # significant_down = significant_down[significant_down["log2FoldChange"] < log2fc_thresh_down]
        # notsignificant = dds[dds["padj"] >= padj_thresh]
        
        # Volcano_plot = ax.scatter(    
        #     x=significant_up["log2FoldChange"],
        #     y=significant_up["padjs_transformed"],
        #     c='darkred', 
        #     alpha=alpha_to_use,
        #     zorder=5,
        # )
        
        # Volcano_plot = ax.scatter(    
        #     x=significant_down["log2FoldChange"],
        #     y=significant_down["padjs_transformed"],
        #     c='navy', 
        #     alpha=alpha_to_use,
        #     zorder=5,
        # )
        
        # Volcano_plot = ax.scatter(    
        #     x=notsignificant["log2FoldChange"],
        #     y=notsignificant["padjs_transformed"],
        #     c='dimgray', 
        #     alpha=alpha_to_use,
        #     zorder=2,
        # )
        
        # ax.set_adjustable("datalim")
        
        # ax.grid(True, alpha=0.4, color='white',linewidth=1.5)
        # ax.set_facecolor('silver')
        # # ax.legend(['label1', 'label2', 'label3'])
        # ax.set_title(processing)
        
        
        # log = False 
        
        # if log is True:
        #     plt.yscale("log")
        #     ax.set_ylim([0.1, 200])
        
        
        # plt.xlabel(r"log$_{2}$ fold change")
        # plt.ylabel(r"-log$_{10}$(p$_{adj}$)")
                   
        
        # plt.tight_layout()
        
        
        # # % MA plot
        
        # colormap = plt.cm.plasma
        
        # padj_thresh = 0.05
        # padjs_transformed = dds["padj"].apply(lambda x: -np.log10(x))
        
        # dds["padjs_transformed"] = dds["padj"].apply(lambda x: -np.log10(x))
        
        # fig, ax = plt.subplots()
        
        # significant = dds[dds["padj"] < padj_thresh]
        # notsignificant = dds[dds["padj"] >= padj_thresh]
        
        # MAplot = ax.scatter(    
        #     x=notsignificant["baseMean"],
        #     y=notsignificant["log2FoldChange"],
        #     c='dimgray', 
        #     alpha=alpha_to_use,
        #     zorder=2,
        # )
        
        # MAplot = ax.scatter(    
        #     x=significant["baseMean"],
        #     y=significant["log2FoldChange"],
        #     c=significant["padjs_transformed"], 
        #     alpha=alpha_to_use,
        #     zorder=3,
            
        # )
        
        # ax.set_adjustable("datalim")
        
        # ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
        # ax.set_facecolor('silver')
        # ax.set_title(processing)
        
        # log = True 
        
        # if log is True:
        #     plt.xscale("log")
        
        # plt.xlabel("mean of normalized counts")
        # plt.ylabel(r"log$_{2}$ fold change")
        
        # plt.tight_layout()
        
        # cbar = fig.colorbar(MAplot, ax=ax, pad=0.03)
        # cbar.set_label("$-\log_{10}(\\text{p}_{\\text{adj}})$", fontsize=12)
        
        
        # # % gene enrichment plot
    
    
        
    
        # colormap = plt.cm.plasma
        
        # fig, ax = plt.subplots()
        
        # rank_plot = ax.scatter(    
        #     x=dds_sorted["rank"],
        #     y=dds_sorted["log2FoldChange"],
        #     c='dimgray', 
        #     alpha=alpha_to_use/4,
        #     zorder=2,
        # )
        
        # rank_plot = ax.scatter(    
        #     x=significant_upregulated["rank"],
        #     y=significant_upregulated["log2FoldChange"],
        #     c='darkred', 
        #     alpha=alpha_to_use/4,
        #     zorder=2,
        # )
        
        # rank_plot = ax.scatter(    
        #     x=significant_downregulated["rank"],
        #     y=significant_downregulated["log2FoldChange"],
        #     c='navy', 
        #     alpha=alpha_to_use/4,
        #     zorder=2,
        # )
        
        
        # gene_set = ax.bar(    
        #     all_annotated_expert_merged_best["rank"],
        #     all_annotated_expert_merged_best["log2FoldChange_goi"],
        #     color=all_annotated_expert_merged_best["f_color"], 
        #     width=20,
        #     alpha=1,
        #     zorder=5,
        #     # label=bar_labels
        # ) 
        
        # ax.set_adjustable("datalim")
        
        # ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
        # ax.set_facecolor('silver')
        # ax.set_title(processing)
    
        
        
        # bar_legend = ax.legend(
        #     handles=[
        #              Patch(facecolor=color, label=function)
        #              for function, color in f_colors.items()
        #     ],
        #     # title="Function",
        #     loc="upper right",
        #     frameon=True
        # )
        
        # ax.add_artist(bar_legend)
        
        # scatter_legend = ax.legend(
        #     handles=[
        #         Line2D(
        #             [0], [0],
        #             marker="o",
        #             linestyle="None",
        #             color="darkred",
        #             label="upregulated",
        #             markersize=8,
        #             alpha = 0.5,
        #         ),
                
        #         Line2D(
        #             [0], [0],
        #             marker="o",
        #             linestyle="None",
        #             color="navy",
        #             label="downregulated",
        #             markersize=8,
        #             alpha = 0.5,
        #         ),
                
        #         Line2D(
        #             [0], [0],
        #             marker="o",
        #             linestyle="None",
        #             color="dimgray",
        #             label="not regulated",
        #             markersize=8,
        #             alpha = 0.5,
        #         )
        #     ],
        #     # title="Regulation",
        #     loc="lower left",
        #     frameon=True
        # )
        
        
        # log = False 
        
        # if log is True:
        #     plt.xscale("log")
        
        # plt.xlabel(r"log$_{2}$ fold change rank")
        # plt.ylabel(r"log$_{2}$ fold change")
        
        # plt.tight_layout()
        
        
        
        # % genome position plot
        
        
        
        # colormap = plt.cm.plasma
        
        # fig, ax = plt.subplots()
        
        # rank_plot = ax.scatter(    
        #     x=dds_sorted["gene_rank"],
        #     y=dds_sorted["log2FoldChange"],
        #     c='dimgray', 
        #     alpha=alpha_to_use/4,
        #     zorder=2,
        # )
        
        # rank_plot = ax.scatter(    
        #     x=significant_upregulated["gene_rank"],
        #     y=significant_upregulated["log2FoldChange"],
        #     c='darkred', 
        #     alpha=alpha_to_use/4,
        #     zorder=2,
        # )
        
        # rank_plot = ax.scatter(    
        #     x=significant_downregulated["gene_rank"],
        #     y=significant_downregulated["log2FoldChange"],
        #     c='navy', 
        #     alpha=alpha_to_use/4,
        #     zorder=2,
        # )
        
        
        # gene_set = ax.bar(    
        #     all_annotated_expert_merged_best["gene_rank"],
        #     all_annotated_expert_merged_best["log2FoldChange_goi"],
        #     color=all_annotated_expert_merged_best["f_color"], 
        #     width=20,
        #     alpha=1,
        #     zorder=5,
        #     # label=bar_labels
        # )
        
        # ax.set_adjustable("datalim")
        
        # ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
        # ax.set_facecolor('silver')
        # ax.set_title(processing)
    
        
        
        # bar_legend = ax.legend(
        #     handles=[
        #              Patch(facecolor=color, label=function)
        #              for function, color in f_colors.items()
        #     ],
        #     # title="Function",
        #     loc="upper right",
        #     frameon=True
        # )
        
        # ax.add_artist(bar_legend)
        
        # scatter_legend = ax.legend(
        #     handles=[
        #         Line2D(
        #             [0], [0],
        #             marker="o",
        #             linestyle="None",
        #             color="darkred",
        #             label="upregulated",
        #             markersize=8,
        #             alpha = 0.5,
        #         ),
                
        #         Line2D(
        #             [0], [0],
        #             marker="o",
        #             linestyle="None",
        #             color="navy",
        #             label="downregulated",
        #             markersize=8,
        #             alpha = 0.5,
        #         ),
                
        #         Line2D(
        #             [0], [0],
        #             marker="o",
        #             linestyle="None",
        #             color="dimgray",
        #             label="not regulated",
        #             markersize=8,
        #             alpha = 0.5,
        #         )
        #     ],
        #     # title="Regulation",
        #     bbox_to_anchor=(1.02, 0.5),
        #     frameon=True
        # )
        
        
        # log = False 
        
        # if log is True:
        #     plt.xscale("log")
        
        # plt.xlabel(r"genome position (gene number)")
        # plt.ylabel(r"log$_{2}$ fold change")
        
        # plt.tight_layout()
        
        
        
        colormap = plt.cm.plasma
        ax = axes[fig_row]
        
        fig_row += 1
        
        # fig, ax = plt.subplots(figsize=(16, 5))
        
        rank_plot = ax.scatter(    
            x=dds_sorted["gene_rank"],
            y=dds_sorted["log2FoldChange"],
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
        
        ax.set_yticks(list(range(-8,10,2)))
        ax.set_ylim([-8,10])
    
        yticks = [-7,9]
    
        ax.vlines(x=significant_upregulated_assimilation_top50['gene_rank'], 
                  ymin=min(yticks), ymax=max(yticks), color=colors[1], 
                  linestyle='--', lw=1.5, alpha=0.5)
        
        ax.vlines(x=significant_upregulated_adaptation_top50['gene_rank'], 
                  ymin=min(yticks), ymax=max(yticks), color=colors[-2], 
                  linestyle='--', lw=1.5, alpha=0.5)
    
        ax.set_adjustable("datalim")
        
        ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
        ax.set_facecolor('darkgray')
        ax.set_title(processing)
    
    
        
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
        
        plt.xlabel(r"genome position (gene number)")
        plt.ylabel(r"log$_{2}$ fold change")
        
        plt.tight_layout()
        
    plt.savefig(f'{in_deseq_path}{genome_processed}_all.png', dpi=600, bbox_inches='tight')
    plt.savefig(f'{in_deseq_path}{genome_processed}_all.svg', bbox_inches='tight')
   
        
        
    # %
    
    
    
    keys = list()
    x = list(range(1,len(genes_of_interest_significant)+1))
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    i = 1
    
    for key, value in genes_of_interest_significant.items():
        
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
    
    
    
    ax.set_adjustable("datalim")
    
    ax.grid(True, alpha=0.4, color='white',linewidth=1.5, zorder=0)
    ax.set_facecolor('silver')
    
    ax.set_xticks(x,keys,rotation = 30)
    
    
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
            
        
        title="gene",
        bbox_to_anchor=(1.02, 0.6),
        frameon=True
        )
    
    accession = '_'.join(key.split('_')[1:3])
    
    plt.xlabel(f'DE comparison: {genome_processed}')
    plt.ylabel(r"log$_{2}$ fold-change")
    
    plt.tight_layout()
    
    plt.savefig(f'{in_deseq_path}{genome_processed}_assimilation.png', dpi=600, bbox_inches='tight')
    plt.savefig(f'{in_deseq_path}{genome_processed}_assimilation.svg', bbox_inches='tight')
    


















