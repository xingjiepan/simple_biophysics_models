#!/usr/bin/env python3


def OD600_to_wet_ecoli_cell_weight(od600):
    '''Convert OD600 to cell density in 
    kg/m^3 which is g/L.
    '''
    return 1.7 * od600 

def ecoli_cell_wet_weight_to_dry_weight(wet_weight):
    '''Convert ecoli cell wet weight to dry weight.'''
    return 0.2 * wet_weight

if __name__ == '__main__':
    pass
