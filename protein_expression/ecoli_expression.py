#!/usr/bin/env python3

ecoli_dry_weight_composition = {
        'protein' : 0.55,
        'RNA' : 0.2, # Mainly from ribosome
        'DNA' : 0.03,
        'lipid' : 0.09,
        'lipopolysaccharide' : 0.03,
        'peptidoglycan' : 0.03,
        'metabolites' : 0.03,
        'inorganic_ions' : 0.01,
        }

def OD600_to_wet_ecoli_cell_weight(od600):
    '''Convert OD600 to cell density in 
    kg/m^3 which is g/L.
    '''
    return 1.7 * od600 

def ecoli_cell_wet_weight_to_dry_weight(wet_weight):
    '''Convert ecoli cell wet weight to dry weight.'''
    return 0.3 * wet_weight

if __name__ == '__main__':
    
    print('OD600=1 ecoli have protein {0} g/L'.format(ecoli_dry_weight_composition['protein'] * ecoli_cell_wet_weight_to_dry_weight(
        OD600_to_wet_ecoli_cell_weight(1))))
