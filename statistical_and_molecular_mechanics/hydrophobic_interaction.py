#!/usr/bin/env python3

surface_tension_coefficients = {
        'water' : 7.28E-2, # N/m, at 20C
        }

AA_side_chain_SASA = { # Angstrom^2
        'ALA':67,
        'PRO':105,
        'VAL':117,
        'LEU':137,
        'ILE':140,
        'MET':160,

        'PHE':175,
        'TYR':187,
        'TRP':217,

        'SER':80,
        'THR':102,
        'CYS':104,

        'HIS':151,
        'LYS':167,
        'ARG':196,
        
        'ASP':106,
        'GLU':138,

        'ASN':113,
        'GLN':144,
        }

def water_surface_energy(surface_area):
    '''Calculate the water surface energy given the surface area.
    The surface area should have unit Angstrom^2. The returned
    energy has unit kcal/mol.
    '''
    return surface_tension_coefficients['water'] * surface_area * 1E-20 * 6.02E23 / 4184

def volume_free_energy(V, P=1E5):
    '''Calculate the free energy of creating a hole of volume V (Angstrom^3)
    at pressure P (Pascal). The surface part of free energy is ignored.
    The returned value has unit kcal/mol.
    '''
    return P * V * 1E-30 * 6.02E23 / 4184

if __name__ == '__main__':
    print('Surface energy for 1 Angstrom^2 is {0} kcal/mol'.format(surface_tension_coefficients['water'] * 1E-20 * 6.02E23 / 4184))

    print('Surface energies for AA side chains:')

    for aa in ['ALA', 'LEU', 'PHE', 'TRP']:
        print('{0}: surface area = {1} Angstrom^2, surface energy = {2:.2f} kcal/mol'.format(
            aa, AA_side_chain_SASA[aa], water_surface_energy(AA_side_chain_SASA[aa])))

    print('\n')

    print('Volume energy for creating a 1 Angstrom^3 hole is {0:.2E} kcal/mol'.format(volume_free_energy(1)))
    print('Volume energy for a cubic protein with 5nm diameter is {0:.2E} kcal/mol'.format(volume_free_energy(50**3)))

