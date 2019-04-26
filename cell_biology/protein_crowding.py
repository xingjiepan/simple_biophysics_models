#!/usr/bin/env python3

import numpy as np
import scipy.special

cell_protein_concentration = 1000 * 0.3 * 0.5 / 3E4 # mol/L 
# (total density 1kg/L) * (wet weight to dry weight) * (protein fraction of dry weight) / (average protein weight 30kDa)

# Increase of free energy due to loss of rotational and translational entropy
# upon binding. The concentration of reactants and products are all 1 mol/L.
binding_rot_trans_G = 30 # kcal/mol

# Estimation of the average protein size
protein_length = 5E-9 # m

# Surface energy for water
water_surface_energy = 0.1 # kcal / mol / Angstrom^2

def mosaic_protein_protein_binding_model():
    '''A model that estimate the binding
    affinities between proteins.
    
    The proteins are estimated as cubes. Each surface
    of a protein are made of a grid of patches with
    sizes of amino acids. Each patch can be either
    hydrophobic, positive charged or negative charged.

    A correct match gives -1 unit energy and a incorrect
    match gives +1 unit energy.
    '''
   
    print('\nMosaic protein protein binding_model:\n')

    # Number of patches per surface. Estimated from that the
    # number of residues is about 300
    num_patches_per_surface = 50 

    # Patch size = 50^2 / 50
    patch_size = 50 # Angstrom^2

    # Energy per patch
    energy_per_patch = 5

    # Kd for perfect match

    print('The Kd for a perfect matched pair is {0:.2e} mol/L'.format(
        np.exp(- (num_patches_per_surface * energy_per_patch - 30) / 0.596)))  #kB * T = 0.596 kcal/mol

    # Number of patches required for mM scale Kd

    print('Binding enthalpy for mM scale Kd is {0:.2f} kcal/mol'.format(
        30 - 0.596 * np.log(1E-3)))

    net_patches_for_mm_kd = 7
    n_positive_patches_for_mm_kd = 29

    # The distribution of number of positive patches is a binomial distribution 

    mean = num_patches_per_surface * 1/3
    std = np.sqrt(num_patches_per_surface * 1/3 * 2/3)

    print('For the distibution of positive matches, mean = {0:.2f}, standard_deviation = {1:.2f}'.format(mean, std))

    z = (n_positive_patches_for_mm_kd - mean) / std

    print('The number of positive patches required of mM scale Kd is {0}, which is {1:.2f} standard deviation from the mean.'.format(
        n_positive_patches_for_mm_kd, z))

    print('The probability of randomly creating mM scale Kd is {0:.2e}'.format((1 - scipy.special.erf(z / np.sqrt(2))) / 2))

    print('\n')

if __name__ == '__main__':

    print('Protein concentration in a cell is about {0} mM'.format(cell_protein_concentration * 1000))


    mosaic_protein_protein_binding_model()
