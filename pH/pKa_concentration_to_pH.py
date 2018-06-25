#!/usr/bin/env python3
'''Calculate pH from pKa of a molecule and its concentration.
Usage:
    ./pKa_concentration_to_pH.py pKa concentration

The concentration should have unit mole per liter.
'''

import sys

import numpy as np


def calc_pH(pKa, concentration):
    '''Calculate pH from pKa of a molecule and its concentration.'''
    Kw = 10 ** (-14)
    Kd = 10 ** (-pKa)

    coeff = [1, Kd, - Kd * concentration - Kw, -Kd * Kw]
    roots = np.roots(coeff)

    # Find the physically meaningful root

    real_roots = [np.real(r) for r in roots if np.imag(r) == 0]

    for root in real_roots:
        if root < 0: continue
        if root - Kw / root < -1E-20: continue
        if root - Kw / root > concentration: continue

        return -np.log10(root)

if __name__ == '__main__':
    pKa = float(sys.argv[1])
    concentration = float(sys.argv[2])

    print('pKa = {0}, concentration = {1}M, pH = {2:.2f}'.format(pKa, concentration, calc_pH(pKa, concentration)))
