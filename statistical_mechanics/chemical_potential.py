#!/usr/bin/env python3

import numpy as np


#Planck's constant 
h = 6.626E-34 # m^2*kg/s

#Boltzmann constant
k_B = 1.38E-23 # m^2*kg/s^2/K


def particle_state_thermal_length(mass, temperature=300):
    '''Calculate the particle state thermal length.
    The thermal length is useful for calculating the single
    partile partition function. In a semi-classic point of
    view, the thermal length is approximately the uncertainty
    length according to Heisenberg's uncertainty principle.
    
    The mass should be in kg and the temperature in K.
    Return the length in m.
    '''
    return h / np.sqrt(2 * np.pi * mass * k_B * temperature) 

def rotation_partion_function(I1, I2, I3, rotation_symmetry=1, temperature=300):
    '''Rotation partition function of a single partical.
    I1, I2 and I3 are the principle moments of inertia.
    '''
    return np.sqrt(np.pi * I1 * I2 * I3) / rotation_symmetry * ((np.sqrt(8 * k_B * temperature) * np.pi / h) ** 3)

if __name__ == '__main__':
    pass
