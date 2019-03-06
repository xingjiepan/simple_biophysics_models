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
        'yeast_num_ribosomes' : 5e5, # N / cell
        'translation_rate' : 5, # aa / sec
        'protein_concentration' : 3e6, # N / um^3
        'yeast_cell_volume': 36, # um^3   
        'yeast_cell_cycle_time': 200, # min

        'hela_average_protein_turnover_rate': 20, # hours 
        'hela_average_protein_cell_cycle': 22, # hours 
        'hela_cell_volume' : 4000, # um^3

        # Energy budget
       
        'atp_cost_per_peptide_bond_formation' : 4,
        'human_fibroblast_atp_production_rate': 1e9, # N / cell / sec
        'atp_per_glucose' : 38,     


        # Thermodynamics

        'human_erythrocyte_atp_concentration' : 5, # mM
        'human_erythrocyte_adp_concentration' : 1, # mM
        'human_erythrocyte_phosphate_concentration' : 15, # mM
        'standard_atp_hydrolysis_free_energy' : -7.3, # kcal/mol

        'peptide_bond_hydrolysis_free_energy' : -3, # kcal/mol
    
        }


def proteostasis():
    print('Proteostasis')
    
    n_proteins_in_yeast = basic_bio_numbers['protein_concentration'] * basic_bio_numbers['yeast_cell_volume']
    max_n_proteins_produced_per_sec = basic_bio_numbers['yeast_num_ribosomes'] * basic_bio_numbers['translation_rate'] / 500 
    protein_doubling_time = n_proteins_in_yeast / max_n_proteins_produced_per_sec 


    print('N proteins in yeast = {0:.2E}'.format(n_proteins_in_yeast))
    print('Yeast max n proteins produced per sec = {0}'.format(max_n_proteins_produced_per_sec))
    print('Yeast protein doubling time = {0} min'.format(protein_doubling_time / 60))

    print('\n')

    n_proteins_in_hela = basic_bio_numbers['protein_concentration'] * basic_bio_numbers['hela_cell_volume']
    hela_protein_synthesis_rate = n_proteins_in_hela * np.log(2) * ( 1 / basic_bio_numbers['hela_average_protein_cell_cycle']
            + 1 / basic_bio_numbers['hela_average_protein_turnover_rate']) 

    print('N proteins in a hela cell = {0:.2E}'.format(n_proteins_in_hela))
    print('Hela cell protein synthesis rate = {0:.2E} sec^-1'.format(hela_protein_synthesis_rate / 3600))

    print('\n\n\n')

def energy_budget():
    print('Energy budget')

    n_proteins_in_hela = basic_bio_numbers['protein_concentration'] * basic_bio_numbers['hela_cell_volume']
    hela_protein_synthesis_rate = n_proteins_in_hela * np.log(2) * ( 1 / basic_bio_numbers['hela_average_protein_cell_cycle']
            + 1 / basic_bio_numbers['hela_average_protein_turnover_rate']) 

    atp_cost_rate_for_protein_synthesis = hela_protein_synthesis_rate * basic_bio_numbers['atp_cost_per_peptide_bond_formation'] * 500
   
    print('Hela cell atp cost rate for protein synthesis = {0:.2E} sec^-1'.format(atp_cost_rate_for_protein_synthesis / 3600))

    glucose_per_sec = basic_bio_numbers['human_fibroblast_atp_production_rate'] / basic_bio_numbers['atp_per_glucose']
    glucose_weight_per_sec = glucose_per_sec * 180.156 / 6.022E23 / 1000 
    fibroblast_volume = 2000 # um^3
    fibroblast_weight = fibroblast_volume * 10E-15
    n_human_cells = 50 / fibroblast_weight
    glucose_weight_per_sec_human = n_human_cells * glucose_weight_per_sec

    print('A human fibroblast consumes {0:.2E} ATPs per second, which is {1:.2E} kg'.format(glucose_per_sec, glucose_weight_per_sec))
    print('The weight of a fibroblast is {0:.2E} kg'.format(fibroblast_weight))
    print('A 50kg human has about {0:.2E} cells, which consumes {1:.2E} kg glucose per second, i.e. {2:.2E}kg glucose per day'.format(n_human_cells, glucose_weight_per_sec_human, glucose_weight_per_sec_human * 3600 * 24))
    print('A human needs {0:.2E} kcal/day. This is a bit over extimated compared with the correct value {1:.2E} kcal/day'.format(glucose_weight_per_sec_human * 3600 * 24 * 4000, 2000))

    print('\n\n\n')

def thermodynamics():
    print('Thermodynamics')

    atp_hydrolysis_free_energy_in_cell = basic_bio_numbers['standard_atp_hydrolysis_free_energy'] + 0.59 * np.log(
            basic_bio_numbers['human_erythrocyte_phosphate_concentration'] * basic_bio_numbers['human_erythrocyte_adp_concentration'] 
            / basic_bio_numbers['human_erythrocyte_atp_concentration'] * 1E-3)   

    print('ATP hydrolysis free energy in cells is {0:.2E} kcal/mol'.format(atp_hydrolysis_free_energy_in_cell))

    print('\n\n\n')


if __name__ == '__main__':

    proteostasis()

    energy_budget()

    thermodynamics()
