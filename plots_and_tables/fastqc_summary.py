# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:12:13 2026

@author: jando & AI
"""

import os
import pandas as pd
import numpy as np


datadir = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/04_qc/"
imgdir = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/Figures/"
datafile = 'fastqc_data.txt'

aggregated_stats = []

# 2. os.walk() goes through all subdirectories inside the base directory
for root, dirs, files in os.walk(datadir):
    
    # Check if the target file exists in the current subdirectory
    if datafile in files:
        # Construct the full file path
        file_path = os.path.join(root, datafile)
        print(f"Parsing: {file_path}")
        
        sample_stats = []
        QS = []
        k = 100

                
        with open(file_path, 'r', encoding='utf-8') as f:
            # 3. Read up to the first 100 lines
            for i in range(52):
                line = f.readline()
                if not line:
                    break # Stop if we reach the end of the file before 100 lines
                
                line_clean = line.strip()
                
                # 4. Extract basic stats
                if line_clean.startswith('Filename'):
                    sample_stats.append(line_clean.split('\t')[1])
                elif line_clean.startswith('Total Sequences'):
                    sample_stats.append(int(line_clean.split('\t')[1]))
                elif line_clean.startswith('%GC'):
                    sample_stats.append(int(line_clean.split('\t')[1]))
                elif line_clean.startswith('#Base'):
                    k = i
                    
                if i>k:
                    QS.append(float(line_clean.split('\t')[1]))
                    
            sample_stats.append(np.mean(QS))
                    
                

        aggregated_stats.append(sample_stats)

agg_stats = pd.DataFrame(aggregated_stats, columns=['Filename','Total Sequences','GC','QS'])

gc = agg_stats['GC'].agg(['mean', 'std', list]).reset_index()
print(f'{gc}')
seq = agg_stats['Total Sequences'].agg(['mean', 'std', list]).reset_index()
print(f'{seq}')
score = agg_stats['QS'].agg(['mean', 'std', list]).reset_index()
print(f'{score}')
