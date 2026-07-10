# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:47:42 2026

@author: DolinsekJ

https://biopython-tutorial.readthedocs.io/en/latest/notebooks/05%20-%20Sequence%20Input%20and%20Output.html#Parsing-or-Reading-Sequences
https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
https://stackoverflow.com/questions/13611065/efficient-way-to-apply-multiple-filters-to-pandas-dataframe-or-series
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import pandas as pd
import sys

in_fasta = sys.argv[1]
in_table = sys.argv[2]
out_fasta_cyn = sys.argv[3]
out_fasta_all = sys.argv[4]
in_ref_proteins = sys.argv[5]
fasta_cols = ['qseqid', 'sseqid', 'pident', 'qcovs','length', 'qlen', 'slen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

cyn_records = []
all_records = []

blast_results = pd.read_table(in_table, names=fasta_cols, index_col=False)
blast_results['qcovs'] = pd.to_numeric(blast_results['qcovs'], errors='coerce')
blast_results_filtered = blast_results[blast_results['qcovs'] >= 70]

blast_qseqids = set(blast_results_filtered['qseqid'])

ref_proteins = pd.read_table(in_ref_proteins)


for seq_record in SeqIO.parse(in_fasta, "fasta"):

    header_in_fasta = seq_record.description
    qseqid = seq_record.id
    
    if qseqid in blast_qseqids:
        
        sseqid = blast_results_filtered.loc[blast_results_filtered["qseqid"] == qseqid, "sseqid"].tolist()[0].split('|')[0]
        ref_protein = ref_proteins.loc[ref_proteins["protein_id"] == sseqid]
                                                                                 
        gene = ref_protein["gene_cur"].tolist()[0]
        protein = ref_protein["protein_cur"].tolist()[0]
        product = ref_protein["protein_names_cur"].tolist()[0]
        organism = ref_protein["source_organism"].tolist()[0]
        pathway = ref_protein["pathway"].tolist()[0]
        dbxrefs = ref_protein["references"].tolist()[0]
        
        cyn_records.append(SeqRecord(Seq(seq_record.seq), id=seq_record.id, description=f'{protein};{product};{pathway}'))   
        all_records.append(SeqRecord(Seq(seq_record.seq), id=seq_record.id, description=f'{protein};{product};{pathway}'))
        
    else:
        
        all_records.append(SeqRecord(Seq(seq_record.seq), id=seq_record.id, description=seq_record.description))

  
SeqIO.write(cyn_records, out_fasta_cyn, "fasta")
SeqIO.write(all_records, out_fasta_all, "fasta")


    
    