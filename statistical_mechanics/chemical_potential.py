#!/usr/bin/env python3

import numpy as np


#Planck's constant 
h = 6.626E-34 # m^2*kg/s

#Boltzmann constant
k_B = 1.38E-23 # m^2*kg/s^2/K

#Avogadro's number
Na = 6.02E23 

def average_molecule_volume(concentration):
    '''Convert concentration in mol/L to average
    volume occupied by each molecule in m^3
    '''
    return 1 / (Na * 1000 * concentration)

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

def translational_free_energy(mass, volume, temperature=300):
    '''Calculate the translational free energy for a
    molecule given the mass and the volume of the container.
    '''
    thermal_length = particle_state_thermal_length(mass, temperature)

    return - k_B * temperature * np.log(volume / (thermal_length ** 3))

if __name__ == '__main__':
    # Print particle thermal lengths

    print('Thermal lengths of particles at 300K:')
    print('    H2 -> {0:.2E} m'.format(particle_state_thermal_length(0.002 / Na)))
    print('    H2O -> {0:.2E} m'.format(particle_state_thermal_length(0.018 / Na)))
    print('    GFP -> {0:.2E} m'.format(particle_state_thermal_length(31 / Na)))
    print('    e-coli -> {0:.2E} m'.format(particle_state_thermal_length(3E8 / Na)))

    # Print the translational free energy

    concentrations = [1, 1E-3, 1E-6, 1E-9]    
    volumes = [average_molecule_volume(c) for c in concentrations]

    print('\nTranslational free energy at 300K:')
    
    print('For water:')
    mass = 0.018 / Na #kg
    for i in range(len(concentrations)):
        print('    concentration = {0:.2E} mol/L, volume = {1:.2E} m^3, translational_free_energy = {2:.2f} k_B*T'.format(
            concentrations[i], volumes[i], translational_free_energy(mass, volumes[i]) / (k_B * 300))) 

    print('For GFP:')
    mass = 31 / Na #kg
    for i in range(len(concentrations)):
        print('    concentration = {0:.2E} mol/L, volume = {1:.2E} m^3, translational_free_energy = {2:.2f} k_B*T'.format(
            concentrations[i], volumes[i], translational_free_energy(mass, volumes[i]) / (k_B * 300))) 

