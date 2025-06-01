from config import os, np, namedtuple, cst, utils

def get_params(dir_main, caso):
    """
    Obtiene en función del caso los parámetros correspondientes.
    
    Args: dir_main, caso
    
    Returns: parámetros separados en estructuras Params_planet: parámetros del planeta, Params_basic: parámetros básicos como la presión o temperatura, Params_prt: parámetros de petitRADTRANS
    
    Nota: el nombre de las estructuras como "Params_prt" va con P mayúscula, el resultado del return es con minúscula "params_prt"
    """
    
    ##########################################################################################
    ###  Notas:  #############################################################################
    ##########################################################################################
    ###  -Primero defino varias estructuras  #################################################
    ###  -dir_data_input = es el directorio donde están los ficheros p-t de cada caso  #######
    ###  -se obtienen las presiones y temperaturas; se dan la vuelta y se pasan a un array  ##
    ###  de numpy porque prt necesita que las presiones vayan de menor a mayor y que sea en  #
    ###  formato numpy  ######################################################################
    ###  -abundances es un diccionario con las especies químicas para calcular las mean_  ####
    ###  _masses  ############################################################################
    ##########################################################################################
    ##########################################################################################
    ##########################################################################################

    Params_planet = namedtuple("Params_planet", "planet_radius_cm reference_gravity_cgs reference_pressure_bar")
    Params_basic = namedtuple("Params_basic","pressures_bar temperatures_K z_km species_labels case_label")

    dir_data_input = os.path.join(dir_main, "..", "data_input")

    if caso == 'ben1':

        data_ben1 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_B1.txt')), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
        data_ben1_flipped = np.flip(data_ben1, axis= 1)

        #Params_planet
        planet_radius_cm = 0.92 * 637100000
        print(planet_radius_cm)

        G_cgs = 6.674 * 10**-8  

        masa_planeta_g = 0.772 * (5.972e27)

        reference_gravity_cgs = ((G_cgs * masa_planeta_g) / (planet_radius_cm** 2))

        print(reference_gravity_cgs)

        reference_pressure_bar = 1
        
        params_planet = Params_planet(
            planet_radius_cm = planet_radius_cm,
            reference_gravity_cgs = reference_gravity_cgs,
            reference_pressure_bar = reference_pressure_bar
            )
        
        #Params_basic
        z_km, pressures_Pa, temperatures_K, Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_ben1_flipped

        pressures_bar = pressures_Pa * 1e-5

        species_labels = ['N2', 'CO2']        

        params_basic = Params_basic(
            pressures_bar = pressures_bar,
            temperatures_K = temperatures_K,
            z_km = z_km,
            species_labels = species_labels,
            case_label = 'ben1'
            )
         
        return params_planet, params_basic

    elif caso == 'ben2':
        
        data_ben2 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_B2.txt')), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
        data_ben2_flipped = np.flip(data_ben2, axis= 1)

        #Params_planet
        planet_radius_cm = 0.92 * 637100000

        G_cgs = 6.674 * 10**-8  

        masa_planeta_g = 0.772 * (5.972e27)

        reference_gravity_cgs = ((G_cgs * masa_planeta_g) / (planet_radius_cm** 2))
        print(reference_gravity_cgs)

        reference_pressure_bar = 1
        
        params_planet = Params_planet(
            planet_radius_cm = planet_radius_cm,
            reference_gravity_cgs = reference_gravity_cgs,
            reference_pressure_bar = reference_pressure_bar
            )
        
        #Params_basic
        z_km, pressures_Pa, temperatures_K, Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_ben2_flipped

        pressures_bar = pressures_Pa * 1e-5
        species_labels = ['N2', 'CO2']
        
        params_basic = Params_basic(
            pressures_bar = pressures_bar,
            temperatures_K = temperatures_K,
            z_km = z_km,
            species_labels = species_labels,
            case_label = 'ben2'           
            )

        return params_planet, params_basic
    
    elif caso == 'hab1':
        
        data_hab1 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_H1.txt')), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
        data_hab1_flipped = np.flip(data_hab1, axis= 1)

        #Params_planet
        planet_radius_cm = 0.92 * 637100000

        G_cgs = 6.674 * 10**-8  

        masa_planeta_g = 0.772 * (5.972e27)

        reference_gravity_cgs = ((G_cgs * masa_planeta_g) / (planet_radius_cm** 2))
        print(reference_gravity_cgs)

        reference_pressure_bar = 1
        
        params_planet = Params_planet(
            planet_radius_cm = planet_radius_cm,
            reference_gravity_cgs = reference_gravity_cgs,
            reference_pressure_bar = reference_pressure_bar
            )
        
        #Params_basic
        z_km, pressures_Pa, temperatures_K, Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_hab1_flipped

        pressures_bar = pressures_Pa * 1e-5
        species_labels = ['N2', 'CO2', 'H2O(l)', 'H2O(s)_crystalline__Mie']
        
        params_basic = Params_basic(
            pressures_bar = pressures_bar,
            temperatures_K = temperatures_K,
            z_km = z_km,
            species_labels = species_labels,
            case_label = 'hab1'           
            )

        return params_planet, params_basic
        
    elif caso == 'ben1_noCO2':

        data_ben1 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_B1.txt')), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
        data_ben1_flipped = np.flip(data_ben1, axis= 1)

        #Params_planet
        planet_radius_cm = 0.92 * 637100000

        G_cgs = 6.674 * 10**-8  

        masa_planeta_g = 0.772 * (5.972e27)

        reference_gravity_cgs = ((G_cgs * masa_planeta_g) / (planet_radius_cm** 2))
        print(reference_gravity_cgs)

        reference_pressure_bar = 1
        
        params_planet = Params_planet(
            planet_radius_cm = planet_radius_cm,
            reference_gravity_cgs = reference_gravity_cgs,
            reference_pressure_bar = reference_pressure_bar
            )
        
        #Params_basic
        z_km, pressures_Pa, temperatures_K, Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_ben1_flipped
        Xmass_CO2 = np.zeros_like(Xmass_CO2)

        pressures_bar = pressures_Pa * 1e-5

        species_labels = ['N2', 'CO2']        

        params_basic = Params_basic(
            pressures_bar = pressures_bar,
            temperatures_K = temperatures_K,
            z_km = z_km,
            species_labels = species_labels,
            case_label = 'ben1_noCO2'
            )
         
        return params_planet, params_basic
    
    else:
        raise ValueError(f"Caso no reconocido: {caso}")

