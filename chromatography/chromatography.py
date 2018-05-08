#!/usr/bin/env python3



def critical_washing_volume(Kd, N_bound, Kd_competitor=None, concentration_competitor=None):
    '''Calculate the critical washing volume at which significantly
    amount of the bound molecule will be washed off.

    Args:
        Kd : Dissociation constant for the bound molecule in mole/L
        N_bound : Mole of bound to the stationary phase
        Kd_competitor : Dissociation constant for the competitor molecule in mole/L
        concentration_competitor : Concentration of the competitor in mole/L

    Return:
        The critical washing volume in L
    '''

    V_no_comp = N_bound / Kd

    if Kd_competitor is None:
        return V_no_comp

    else:
        v_comp = (N_bound * Kd_competitor) / (Kd * concentration_competitor)
        
        return min(V_no_comp, v_comp)
