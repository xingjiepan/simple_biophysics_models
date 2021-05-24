#!/usr/bin/env python3

reaction_rates = [
        {'reaction':'atp_hydrolysis', 'buffer':'water', 't_half':'116 hours'},
        {'reaction':'atp_hydrolysis', 'buffer':'Mg2+_pH1.52', 't_half':'42 min'},
        {'reaction':'atp_hydrolysis', 'buffer':'Mg2+_pH6.59', 't_half':'27.8 hours'},
        {'reaction':'atp_hydrolysis', 'buffer':'Ca2+_pH1.40', 't_half':'40 min'},
        {'reaction':'atp_hydrolysis', 'buffer':'Ca2+_pH7.01', 't_half':'5.8 hours'},
        
        {'reaction':'DNA_hydrolysis', 'buffer':'water', 't_half':'30,000,000 years'}, # The rate is at pH=7. # Gates, K. S. (2009). An overview of chemical processes that damage cellular DNA: spontaneous hydrolysis, alkylation, and reactions with radicals. Chemical research in toxicology, 22(11), 1747-1760.
        
        {'reaction':'peptide_bond_hydrolysis', 'buffer':'water', 't_half':'7 years'}, # Other sources said 350 to 600 years
        ]
