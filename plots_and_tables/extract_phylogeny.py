# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:47:42 2026

@author: DolinsekJ


"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import pandas as pd
import numpy as np

# in_table = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/4_STO/genomes/gtdbtk.bac120.summary.tsv"
in_table = "C:/Dropbox/FHWN/M.BDSC.B.23.AA Masterarbeit/MG/4_STO/gtdbtk.bac120.summary.tsv"

phylo = pd.read_table(in_table)

def safe_apply(fn, default=np.nan):
    def wrapper(x):
        try:
            return fn(x)
        except Exception:
            return default
    return wrapper

phylo['id'] = phylo['user_genome'].apply(safe_apply(lambda x: x.split('.')[0]))
phylo['rank'] = phylo['classification'].apply(safe_apply(lambda x: x.split(';')[-1].split('__')[0]))
phylo['name'] = phylo['classification'].apply(safe_apply(lambda x: x.split(';')[-1].split('__')[1]))

# phylo_interest = phylo[['id', 'rank','name']] # use for genomes
phylo_interest = phylo[['user_genome', 'rank','name']] # use for MAGs/bins

phylo_interest.to_excel(f'{in_table}.xlsx', sheet_name="Sheet1")