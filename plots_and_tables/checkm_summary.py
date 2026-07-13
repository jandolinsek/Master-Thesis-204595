# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:12:13 2026

@author: jando & AI
"""

import os
import pandas as pd
import ast
import numpy as np

datadir = []
datadir.append("C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/1_SIE/genomes/") # C:\Users\dolinsekj\
datadir.append("C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/9_SIM/genomes/") # C:\Users\dolinsekj\
datadir.append("C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/SO4_STO/genomes/") # C:\Users\dolinsekj\
imgdir = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/Figures/"
datafile = 'bin_stats_ext.tsv'
resultfile = 'bin_stats.xlsx'

for directory in datadir:

    file_path = os.path.join(directory, datafile)
    
    # read two columns: bin id and the Python-dict-like string
    df = pd.read_csv(file_path, sep="\t", header=None, names=["bin", "meta"], dtype={"bin": str}, engine="python")
    
    # convert string->dict safely, then normalize into columns, needed as not a clean json file
    df["meta"] = df["meta"].apply(ast.literal_eval)
    meta_df = pd.json_normalize(df["meta"])
    
    # final dataframe: keep bin + expanded metadata
    result = pd.concat([df[["bin"]].reset_index(drop=True), meta_df.reset_index(drop=True)], axis=1)
    
    final_result = result.filter(items=["bin","marker lineage","# markers","Completeness","Contamination","GC","Genome size","# contigs","N50 (contigs)","Mean contig length","# predicted genes"])
    final_result.rename(columns={"marker lineage": "Taxonomy"}, inplace=True)
    final_result.rename(columns={"bin": "Bin"}, inplace=True) 
    final_result.rename(columns={"# markers": "Markers"}, inplace=True)    
    final_result.rename(columns={"# contigs": "Contigs"}, inplace=True) 
    final_result.rename(columns={"N50 (contigs)": "N50 (kb)"}, inplace=True) 
    final_result.rename(columns={"# predicted genes": "Predicted genes"}, inplace=True)  
    final_result.rename(columns={"Mean contig length": "Mean contig length (kb)"}, inplace=True) 
    final_result.rename(columns={"Genome size": "Genome size (kb)"}, inplace=True) 
    final_result.rename(columns={"GC": "GC (%)"}, inplace=True) 
   
    final_result["GC (%)"]=final_result["GC (%)"]*100
    final_result["Mean contig length (kb)"]=final_result["Mean contig length (kb)"]/1000
    final_result["Genome size (kb)"]=final_result["Genome size (kb)"]/1000
    final_result["N50 (kb)"]=final_result["N50 (kb)"]/1000
    
    final_result["Bin"]=final_result["Bin"].str.split('.').str[0]
        
    final_result["GC (%)"]=np.round(final_result["GC (%)"], decimals=1, out=None)
    final_result["Completeness"]=np.round(final_result["Completeness"], decimals=1, out=None)
    final_result["Contamination"]=np.round(final_result["Contamination"], decimals=1, out=None)
    final_result["Mean contig length (kb)"]=np.round(final_result["Mean contig length (kb)"], decimals=0, out=None)
    final_result["N50 (kb)"]=np.round(final_result["N50 (kb)"], decimals=0, out=None)
    final_result["Genome size (kb)"]=np.round(final_result["Genome size (kb)"], decimals=0, out=None)

    final_result.sort_values("Completeness", ascending=False)  
    
    final_result.to_excel(os.path.join(directory, resultfile), sheet_name="Sheet1")