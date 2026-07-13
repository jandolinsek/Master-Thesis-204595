

import pandas as pd
import numpy as np
import os
# from os import path
import pickle

import matplotlib.pyplot as plt



# % Calculate relative abundances from the FeatureCounts data

# enrichments = ['9_SIM','1_SIE','4_STO']
enrichments = ['1_SIE']


for enrichment in enrichments:
    paths = ['C:', 'C:/Users/dolinsekj', 'C:/Users/jando/OneDrive']
    path = 1
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
    
    
    dirs_tmp = os.listdir(in_deseq_path)
    dirs_tmp = [in_deseq_path + dir_tmp + '/' for dir_tmp in dirs_tmp]
    
    dirs_indeed = [item for item in dirs_tmp if os.path.isdir(item)]
    
    
    genomes_deseq = dict()

    

    for dir_tmp in dirs_indeed:
        
        dir_tmp = dirs_indeed[0]
        
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
        comparisons = dict()
        gene_sets = dict()
        
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
        
        
        for file_dds in files_dds:
            
            # file_dds = files_dds[-2]
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
            
            all_annotated_expert_merged = pd.merge(all_annotated, blast_annotated, on="Geneid", how="left")
            
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
                
            all_annotated_expert_merged_best_box = all_annotated_expert_merged_best[all_annotated_expert_merged_best['padj'] < padj_thresh]
            significant_expert_bool=all_annotated_expert_merged_best_box["pident"].notna()
            significant_expert=all_annotated_expert_merged_best_box[significant_expert_bool]
            
            all_annotated_top50_assimilation = pd.merge(all_annotated_expert_merged_best, significant_upregulated_assimilation_top50, on="gene_number", how="right")
            all_annotated_top50_adaptation = pd.merge(all_annotated_expert_merged_best, significant_upregulated_adaptation_top50, on="gene_number", how="right")
           
               
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
               
            
            # nan_mask = all_annotated_expert_merged_best['Age'].isna()
            # all_annotated_expert_merged_best.loc[nan_mask, 'Age'] = all_annotated.loc[nan_mask, 'Age']
     
            
            # comparisons[processing] = all_annotated_expert_merged_best
            
            gene_sets['adaptation'] = all_annotated_top50_adaptation
            gene_sets['assimilation'] = all_annotated_top50_assimilation
            
            comparisons[processing] = [all_annotated_expert_merged_best, gene_sets]

           
            
            genomes_deseq[genome_processed] = [genes_of_interest_significant, 
                                               # significant_upregulated_adaptation_top50,
                                               # significant_upregulated_assimilation_top50,
                                               comparisons                                           
                                               ]
             
      
    with open(f"{in_deseq_path}genomes_deseq.pkl", "wb") as f:
        pickle.dump(genomes_deseq, f)
        
        
        

