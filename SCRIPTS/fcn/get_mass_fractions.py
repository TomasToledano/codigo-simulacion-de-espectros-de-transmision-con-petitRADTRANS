from config import np

def get_mass_fractions(modo, params_basic, params_Xmass_species, params_fastchem):
    species_molar_masses = {
        'H2O': 18.01528,
        'CH4': 16.04,
        'CO': 28.01,
        'CO2': 44.01,
        'N2': 28.0112,
        'O2': 31.99,
        'O': 15.99
    }

    normal_to_fastchem = {
        "CO": "C1O1",
        "CH4": "C1H4",
        "CO2": "C1O2",
        "N2": "N2",
        "H2O": "H1O2",
        "O2": "O2",
        "O": "O"
    }

    mass_fractions = {}

    if modo == 'fastchem':
        species_labels_deseadas = ["CO", "CO2", "N2", "CH4", "H2O", "O2"]

        total_mass_frac = np.zeros_like(params_fastchem.number_densities_molec_m3[:, 0])
        
        for species in species_labels_deseadas:
            fastchem_name = normal_to_fastchem[species]  # convierto nombre normal a FastChem
            idx = params_fastchem.species_to_index[fastchem_name]  # índice en FastChem
            
            frac_molar_i = params_fastchem.number_densities_molec_m3[:, idx] / params_fastchem.gas_number_density_molec_m3
            mass_i = species_molar_masses[species]
            total_mass_frac += frac_molar_i * mass_i

        for species in species_labels_deseadas:
            fastchem_name = normal_to_fastchem[species]
            idx = params_fastchem.species_to_index[fastchem_name]

            frac_molar_i = params_fastchem.number_densities_molec_m3[:, idx] / params_fastchem.gas_number_density_molec_m3
            mass_i = species_molar_masses[species]
            mass_fractions[species] = (mass_i * frac_molar_i) / total_mass_frac

        return mass_fractions

    elif modo == 'fichero':
        
        if params_basic.case_label == 'ben1_noCO2':
            
            mass_fractions['N2'] = params_Xmass_species.Xmass_N2
            mass_fractions['CO2'] = np.zeros_like(params_Xmass_species.Xmass_CO2)
            
        elif params_basic.case_label == 'hab1':
            
            mass_fractions['N2'] = params_Xmass_species.Xmass_N2
            mass_fractions['CO2'] = params_Xmass_species.Xmass_CO2
            mass_fractions['H2O(l)'] = params_Xmass_species.Xmass_H2O_l
            mass_fractions['H2O(s)_crystalline__Mie'] = params_Xmass_species.Xmass_H2O_s                
            
        else:
            
            mass_fractions['N2'] = params_Xmass_species.Xmass_N2
            mass_fractions['CO2'] = params_Xmass_species.Xmass_CO2

        return mass_fractions




