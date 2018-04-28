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


water_viscosity = 0.001 

def friction_coefficient_for_sphere(radius, viscosity=water_viscosity):
    '''Get the friction coefficient for a sphere.
    The radius is in meter. The viscosity is kg / (s * m) 

    friction = 6 * pi * viscosity * radius
    '''
    return 6 * np.pi * viscosity * radius 

def diffusion_coefficient(friction_coefficient, temperature=300):
    '''Get the diffusion_coefficient in m^2 / s

    diffusion_coefficient = k * temperature / friction_coefficient
    '''
    k = 1.38 * (10 ** (-23))

    return k * temperature / friction_coefficient 

if __name__ == '__main__':

    for d in experimental_diffusion_constants:
        r = weight_to_radius(d['weight'])
        friction_coefficient = friction_coefficient_for_sphere(r)
        D = diffusion_coefficient(friction_coefficient)
        print('molecule:{0}, radius = {1:.2E} m, D_measure = {2:.2E} m^2/s, D_calc = {3:.2E} m^2/s'.format(
            d['molecule'], r, d['D'], D))
