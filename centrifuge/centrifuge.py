#!/usr/bin/env python3

import numpy as np

# weights are in Dalton. Densities are in kg/(m^3)
particles = [
        {'molecule':'GFP', 'weight':3.1E4, 'density':1300},
        {'molecule':'DNA', 'weight':6E6, 'density':2000}, # Length ~10 kbp
        {'molecule':'tobacco_mosaic_virus', 'weight':5E7, 'density':1150},
        {'molecule':'e-coli_genome', 'weight':6E8, 'density':2000}, # Length ~10 kbp
        {'molecule':'e-coli', 'weight':3E11, 'density':1090},
        ]

centrifuges = [
        {'name':'nothing', 'g':10},
        {'name':'convenience', 'g':21100},
        {'name':'quick', 'g':30279},
        {'name':'fast', 'g':1048680},
        ]

def boltzmann_decay_length(g, weight_Da, density, temperature=300, solvent_density=1000):
    '''Calcuate the decay length for particle in
    a centrifuge.
    Given g m/(s^2), weight Dalton, density kg/(m^3).
    Return the decay length in m.
    '''
    k = 1.38 * (10 ** (-23))
    Na = 6.02 * (10 ** 23)

    weight_kg = weight_Da / Na / 1000
    adjusted_weight = weight_kg * (1 - solvent_density / density) 

    return k * temperature / adjusted_weight / g 

def weight_to_radius(weight):
    '''Calculate the radius of a molecule from its
    weight. Assume that the density of the molecule
    is same to water and the molecule is spherical.

    The weight is in Dalton and the radius is in meter.
    '''
    Na = 6.02 * (10 ** 23)
    density = 1000 # kg / m^3

    volume = weight / Na / 1000 / density

    return (volume * 3 / 4 / np.pi) ** (1 / 3)


if __name__ == '__main__':

    for c in centrifuges:
        print(c)
        for p in particles:
            print('molecule {0}, weight = {1:.2E} Da, density = {2:.3E} kg/m^3, radius = {3:.2E}, decay_length = {4:.2E} m'.format(
                p['molecule'], p['weight'], p['density'], weight_to_radius(p['weight']), 
                boltzmann_decay_length(c['g'], p['weight'], p['density'])))

        print('\n')

