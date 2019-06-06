#!/usr/bin/env python3

import numpy as np

#Boltzmann constant
k_B = 1.38E-23 # m^2*kg/s^2/K

#Avogadro's number
Na = 6.02E23 

#Unit charge
e = 1.6021765E-19 #Coulomb

#Vaccum permittivity
epsilon_0 = 8.8541878128E-12 #F*m^-1

def joule_to_kcal_per_mol(J):
    '''Conver energy in joule to kcal/mol'''
    return J * 6.02E23 / 4184 

def coulomb_potential(q1, q2, r, dielectric_constant=1):
    '''Calculate the coulomb potential between two point
    charges q1, q2 separated by distance r. Units are:
        q1, q2: unit charge
        r: angstrom
        return value: kcal/mol
    '''
    return joule_to_kcal_per_mol(1 / (4 * np.pi * epsilon_0 * dielectric_constant) * q1 * e * q2 * e / (r * 1E-10))

def debye_length(z, n, T, epsilon):
    '''Calculate the Debye length for charges in solution with ions.
    z: valency of the ions,
    n: concentration of the ion in mole/L.
    T: temperature in K.
    epsilon: the relative dielectric constant.
    
    Return the Debye length in meters.
    '''
    return np.sqrt(epsilon * epsilon_0 * k_B * T / (2 * z**2 * e**2 * n * Na * 1000) )

def lennard_jones_potential(e1, e2, r1, r2, r):
    '''Calculate the lennard jones potential.
    e1, e2: The lowest potential of atoms
    r1, r1: Lowest energy distances of atoms in angstrom
    r: distance between atoms in angstrom

    Return the L-J potential in the unit of e1 and e2.
    '''
    e_mean = np.sqrt(e1 * e2)
    r_mean = (r1 + r2) / 2

    return e_mean * ((r_mean / r)**12 - 2 * (r_mean / r)**6) 

LJ_params = { # r in angstroms and e in kcal/mol
        'O' : {'r' : 2.96, 'e' : 0.21},
        'N' : {'r' : 3.25, 'e' : 0.17},
        'C' : {'r' : 3.5, 'e' : 0.08},
        'H' : {'r' : 2.5, 'e' : 0.05},
        }

if __name__ == '__main__':
    
    # Electrostatics

    print("The electrostatic potential between two unit charges separated by 3 Angstrom in vacuum is {0:.2f} kcal/mol".format(
        coulomb_potential(1, 1, 3)))
    print("The electrostatic potential between two unit charges separated by 3 Angstrom in protein is {0:.2f} kcal/mol".format(
        coulomb_potential(1, 1, 3, 5)))
    print("The electrostatic potential between two unit charges separated by 3 Angstrom in water is {0:.2f} kcal/mol".format(
        coulomb_potential(1, 1, 3, 80)))

    print('')

    for n in [1E-6, 1E-3, 0.1, 1]:    
        print("The Debye length for {0:.2E} M NaCl solution is {1:.3E} m".format(n, debye_length(1, n, 300, 80)))

    print('\n')

    # Lennard-Jones

    print("The LJ potential between two C atoms at distance 3.5 angstrom is {0:.2f} kcal/mol".format(
        lennard_jones_potential(LJ_params['C']['e'], LJ_params['C']['e'], LJ_params['C']['r'], LJ_params['C']['r'], 3.5)))
