#!/usr/bin/env python3
'''Basic bio-numbers in a cell.
'''

import numpy as np

basic_bio_numbers = {
        # Replication
        'dna_replication': 2, # kb/min
        'mean_human_chromosome_size': 128327, # kb
        'hela_s_phase_duration': 530, # min
        'mammals_mean_inter_ORI_inverval_length': 40, # kb
        
        # Proteostasis

        'yeast_num_mrna' : 15000, # N / cell
        'yeast_num_ribosomes' : 500000, # N / cell
        'translation_rate' : 5, # aa / sec
        'protein_concentration' : 3000000, # N / um^3
        'yeast_cell_volume': 36, # um^3   
        'yeast_cell_cycle_time': 200, # min

        'hela_average_protein_turnover_rate': 20, # hours 
        'hela_average_protein_cell_cycle': 22, # hours 
        'hela_cell_volume' : 4000, # um^3

        # Energy budget
       
        'atp_cost_per_peptide_bond_formation' : 4,
        'human_fibroblast_atp_production_rate': 1e9, # N / cell / sec
         

        }


def proteostasis():
    print('Proteostasis')
    
    n_proteins_in_yeast = basic_bio_numbers['protein_concentration'] * basic_bio_numbers['yeast_cell_volume']
    max_n_proteins_produced_per_sec = basic_bio_numbers['yeast_num_ribosomes'] * basic_bio_numbers['translation_rate'] / 500 
    protein_doubling_time = n_proteins_in_yeast / max_n_proteins_produced_per_sec 


    print('N proteins in yeast = {0}'.format(n_proteins_in_yeast))
    print('Yeast max n proteins produced per sec = {0}'.format(max_n_proteins_produced_per_sec))
    print('Yeast protein doubling time = {0} min'.format(protein_doubling_time / 60))

    print('\n')

    n_proteins_in_hela = basic_bio_numbers['protein_concentration'] * basic_bio_numbers['hela_cell_volume']
    hela_protein_synthesis_rate = n_proteins_in_hela * np.log(2) * ( 1 / basic_bio_numbers['hela_average_protein_cell_cycle']
            + 1 / basic_bio_numbers['hela_average_protein_turnover_rate']) 

    print('N proteins in a hela cell = {0}'.format(n_proteins_in_hela))
    print('Hela cell protein synthesis rate = {0} sec^-1'.format(hela_protein_synthesis_rate / 3600))

    print('\n\n\n')

def energy_budget():
    print('Energy budget')

    n_proteins_in_hela = basic_bio_numbers['protein_concentration'] * basic_bio_numbers['hela_cell_volume']
    hela_protein_synthesis_rate = n_proteins_in_hela * np.log(2) * ( 1 / basic_bio_numbers['hela_average_protein_cell_cycle']
            + 1 / basic_bio_numbers['hela_average_protein_turnover_rate']) 

    atp_cost_rate_for_protein_synthesis = hela_protein_synthesis_rate * basic_bio_numbers['atp_cost_per_peptide_bond_formation'] * 500
   
    print('Hela cell atp cost rate for protein synthesis = {0:.2E} sec^-1'.format(atp_cost_rate_for_protein_synthesis / 3600))

    print('\n\n\n')

if __name__ == '__main__':

    proteostasis()

    energy_budget()
