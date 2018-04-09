#!/usr/bin/env python3

import numpy as np


# Temperatures are in Kelvin, weights are in Dalton, Ds are in m^2 / s
experimental_diffusion_constants = [
        {'molecule':'H2', 'medium':'water', 'temperature':298, 'weight':2, 'D':4.5 * (10 ** (-9))},
        {'molecule':'water', 'medium':'water', 'temperature':298, 'weight':18, 'D':2.13 * (10 ** (-9))},
        {'molecule':'O2', 'medium':'water', 'temperature':298, 'weight':32, 'D':2.1 * (10 ** (-9))},
        {'molecule':'urea', 'medium':'water', 'temperature':298, 'weight':60, 'D':1.38 * (10 ** (-9))},
        {'molecule':'benzene', 'medium':'water', 'temperature':298, 'weight':78, 'D':1.02 * (10 ** (-9))},
        {'molecule':'sucrose', 'medium':'water', 'temperature':298, 'weight':342, 'D':5.23 * (10 ** (-10))},
        {'molecule':'GFP', 'medium':'water', 'temperature':298, 'weight':31000, 'D':8.7 * (10 ** (-11))},
        {'molecule':'DNA', 'medium':'water', 'temperature':293, 'weight':6000000, 'D':1.3 * (10 ** (-12))},
        {'molecule':'tobacco_mosaic_virus', 'medium':'water', 'temperature':293, 'weight':50000000, 'D':3 * (10 ** (-12))},
        ]


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

    for d in experimental_diffusion_constants:
        print('molecule:{0}, radius = {1:.2E}m'.format(
            d['molecule'], weight_to_radius(d['weight'])))
