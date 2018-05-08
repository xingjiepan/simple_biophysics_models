#!/usr/bin/env python3

import numpy as np


# Temperatures are in Kelvin, weights are in Dalton, Ds are in m^2 / s
experimental_diffusion_constants = [
        {'molecule':'H2', 'medium':'water', 'temperature':298, 'weight':2, 'D':4.5E-9},
        {'molecule':'water', 'medium':'water', 'temperature':298, 'weight':18, 'D':2.13E-9},
        {'molecule':'O2', 'medium':'water', 'temperature':298, 'weight':32, 'D':2.1E-9},
        {'molecule':'urea', 'medium':'water', 'temperature':298, 'weight':60, 'D':1.38E-9},
        {'molecule':'benzene', 'medium':'water', 'temperature':298, 'weight':78, 'D':1.02E-9},
        {'molecule':'sucrose', 'medium':'water', 'temperature':298, 'weight':342, 'D':5.23E-10},
        {'molecule':'GFP', 'medium':'water', 'temperature':298, 'weight':3.1E4, 'D':8.7E-11},
        {'molecule':'DNA', 'medium':'water', 'temperature':293, 'weight':6E6, 'D':1.3E-12}, # Length ~10 kbp
        {'molecule':'tobacco_mosaic_virus', 'medium':'water', 'temperature':293, 'weight':5E7, 'D':3E-12},
        {'molecule':'e-coli', 'weight':3E11, 'D': 2E-13, 'D_active':4E-10},
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

def thermal_velocity(weight_Da, temperature=300):
    '''Calculate the thermal velocity given the weight
    of a particle. The weight should be in Dalton.
    '''
    k = 1.38 * (10 ** (-23))
    Na = 6.02 * (10 ** 23)

    weight_kg = weight_Da / Na / 1000

    return np.sqrt(2 * k * temperature / weight_kg) 

def diffusion_limited_reaction_rate(D1, r1, D2, r2):
    '''Calculate the diffusion limited reaction rate
    k = 4 * pi * (D1 + D2) * (r1 + r2)
    '''
    return 4 * np.pi * (D1 + D2) * (r1 + r2)

def diffusion_limited_reaction_rate_for_same_spheres(viscosity=water_viscosity, temperature=300):
    '''Calculate the diffusion limited reaction rate for
    same spheres.

    k = 16 * pi * D * r
      = 16 * pi * kB * temperature / friction_coefficient * r
      = 16 * pi * kB * temperature / (6 * pi * viscosity * r) * r
      = 8 / 3 * kB * temperature / viscosity

    The unit of k is m^3 / s
    '''
    kB = 1.38 * (10 ** (-23))
    return 8 / 3 * kB * temperature / viscosity

def diffusion_limited_off_rate_for_same_spheres(Kd):
    '''Calculate the diffusion limited off rate for same spheres
    given the Kd. The unit of Kd is m^(-3).
    Return k_off in s^(-1)
    '''
    k_on = diffusion_limited_reaction_rate_for_same_spheres()
    return k_on * Kd


if __name__ == '__main__':

    for d in experimental_diffusion_constants:
        r = weight_to_radius(d['weight'])
        friction_coefficient = friction_coefficient_for_sphere(r)
        D = diffusion_coefficient(friction_coefficient)
        print('molecule:{0}, radius = {1:.2E} m, D_measure = {2:.2E} m^2/s, D_calc = {3:.2E} m^2/s, v = {4:.2E} m/s'.format(
            d['molecule'], r, d['D'], D, thermal_velocity(d['weight'])))

    print('\nThe diffusion limited reaction rate for same spheres in water is {0:.3E} m^3/s'.format(
    diffusion_limited_reaction_rate_for_same_spheres()))


    print('\nThe diffusion limited off rate for different Kd are:')
    for Kd in [1, 1E-3, 1E-6, 1E-9, 1E-12]:
        Kd_std_unit = Kd * 6.02E23 / 0.001
        k_off = diffusion_limited_off_rate_for_same_spheres(Kd_std_unit)
        t = 1 / k_off
        print('Kd = {0} L/mol, k_off = {1}, t = {2}'.format(Kd, k_off, t))

