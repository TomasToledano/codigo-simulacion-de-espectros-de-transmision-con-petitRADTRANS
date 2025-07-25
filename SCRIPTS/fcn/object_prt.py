from config import Radtrans, np

def object_prt(aerosol, params_basic, modo):
    """
    Devuelve el objeto radtrans guardado en la variable atmosphere que se usará para hacer espectros.

    Notas: se guardan en excluded_species el helio y N2 para no añadirlos a line_species, prt no lo añade porque es químicamente inerte, sí que afecta 
    en los choques, en mass fractions y en peso molecular medio.
    
    Args: params_basic porque se necesita la presión y las especies químicas que se van a usar

    Return: objeto RADTRANS guardado en la variable atmosphere.

    """
    species_labels_deseadas = ["CO", "CO2", "N2", "CH4", "H2O", "O2"]

    if modo == 'fastchem':
        line_species = []

        # Conjunto con especies a excluir porque prt no utiliza N2 para lineas
        excluded_species = {"He", "N2"}

        for element in species_labels_deseadas:
            if element not in excluded_species:
                line_species.append(f"{element}.R100")

        atmosphere = Radtrans(
            pressures=params_basic.pressures_bar,
            wavelength_boundaries=[0.1, 50],
            line_species=line_species,
            rayleigh_species=["N2", "CO2", "CO", "CH4", "H2O", "O2"],
            gas_continuum_contributors=['CO2--CO2','N2--N2','O2--O2']
        )

        return atmosphere
            
    else:
        
        if aerosol == 'no':
            line_species = []
            
            # Conjunto con especies a excluir porque prt no utiliza N2 para lineas
            excluded_species = {"He", "N2"}  

            for elements in params_basic.species_labels:
                if elements not in excluded_species:
                    line_species.append(f"{elements}.R100")

                    atmosphere = Radtrans(
                        pressures=params_basic.pressures_bar,
                        wavelength_boundaries=[0.1, 50],
                        line_species = line_species,
                        rayleigh_species=['N2', 'CO2'],
                        gas_continuum_contributors=['CO2--CO2','N2--N2']
                    )
      
                    return atmosphere
            
        elif aerosol == 'si':
        
            line_species = []
            
            # Conjunto con especies a excluir porque prt no utiliza N2 para lineas
            excluded_species = {"He", "N2"}

            for elements in params_basic.species_labels:
                if elements not in excluded_species:
                    line_species.append(f"{elements}.R100")
                
                    atmosphere = Radtrans(
                        pressures=params_basic.pressures_bar,
                        wavelength_boundaries=[0.6, 50],
                        line_species = line_species,
                        rayleigh_species=['N2','CO2','H2O'],
                        gas_continuum_contributors=['N2--N2', 'CO2--CO2', 'H2O--H2O', 'N2-H2O'],
                        cloud_species = ['H2O(s)_crystalline__Mie','H2O(l)']
                    )
            
                    return atmosphere
        



            

            
   


            
