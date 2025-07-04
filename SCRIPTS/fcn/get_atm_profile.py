from config import os, np, cst, namedtuple
from names2names_fastchem import names2names_fastchem

def get_atm_profile(caso, modo,  dir_main, params_basic):
    """
    Devuelve: en el modo fichero las fracciones en masa de las especies y aerosoles sacadas de los ficheros; en el modo fastchem:los parámetros necesarios para posteriormente obtener la fracción en masa en petitRADTRANS.

    Args: caso, modo, species_labels: para usar la fcn names2names_fastchem, dir_main: para poder acceder a los directorios de fastchem, params_basic: necesario para realizar el equilibrio químico con fastchem (contiene el array de presiones y temperaturas).
    
    Returns: params_Xmass_species y params_fastchem: estas son dos estructuras que guardan, en el caso de params_Xmass_species las fracciones en masa y params_fastchem las variables necesarias para calcular la fracción en masa posteriormente con get_mass_fractions.
    """
    
    dir_data_input = os.path.join(dir_main, "..", "data_input")
    
    data_ben1 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_B1.txt')), unpack = True, skiprows = 1, usecols = (3,4,5,6))
    data_ben1_flipped = np.flip(data_ben1, axis= 1)
    
    data_ben2 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_B2.txt')), unpack = True, skiprows = 1, usecols = (3,4,5,6))
    data_ben2_flipped = np.flip(data_ben2, axis= 1)

    data_hab1 = np.loadtxt((os.path.join(dir_data_input,'vertical_profiles_termin_avg_Trappist1e_H1.txt')), unpack = True, skiprows = 1, usecols = (3,4,5,6))
    data_hab1_flipped = np.flip(data_hab1, axis= 1)

    if modo == 'fichero':

        params_fastchem = None

        if caso == 'ben1':

            Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_ben1_flipped

            Params_Xmass_species = namedtuple("Params_Xmass_species", "Xmass_N2 Xmass_CO2 Xmass_H2O_l Xmass_H2O_s")

            params_Xmass_species = Params_Xmass_species(
                Xmass_N2 = Xmass_N2,
                Xmass_CO2 = Xmass_CO2,
                Xmass_H2O_l = Xmass_H2O_l,
                Xmass_H2O_s = Xmass_H2O_s
            )
                       
            return params_Xmass_species, params_fastchem
        
        if caso == 'ben2':

            Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_ben2_flipped
            
            Params_Xmass_species = namedtuple("Params_Xmass_species", "Xmass_N2 Xmass_CO2 Xmass_H2O_l Xmass_H2O_s")

            params_Xmass_species = Params_Xmass_species(
                Xmass_N2 = Xmass_N2,
                Xmass_CO2 = Xmass_CO2,
                Xmass_H2O_l = Xmass_H2O_l,
                Xmass_H2O_s = Xmass_H2O_s
            )
            
            return params_Xmass_species, params_fastchem

        if caso == 'ben1_noCO2':

            Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_ben1_flipped
            
            Params_Xmass_species = namedtuple("Params_Xmass_species", "Xmass_N2 Xmass_CO2 Xmass_H2O_l Xmass_H2O_s")

            params_Xmass_species = Params_Xmass_species(
                Xmass_N2 = Xmass_N2,
                Xmass_CO2 = Xmass_CO2,
                Xmass_H2O_l = Xmass_H2O_l,
                Xmass_H2O_s = Xmass_H2O_s
            )
            
            return params_Xmass_species, params_fastchem

        if caso == 'hab1':

            Xmass_N2, Xmass_CO2, Xmass_H2O_l, Xmass_H2O_s = data_hab1_flipped
            
            Params_Xmass_species = namedtuple("Params_Xmass_species", "Xmass_N2 Xmass_CO2 Xmass_H2O_l Xmass_H2O_s")

            params_Xmass_species = Params_Xmass_species(
                Xmass_N2 = Xmass_N2,
                Xmass_CO2 = Xmass_CO2,
                Xmass_H2O_l = Xmass_H2O_l,
                Xmass_H2O_s = Xmass_H2O_s
            )
            
            return params_Xmass_species, params_fastchem
        
    
        
        ###########################################################################################
        ######  FastChem  #########################################################################
        ###########################################################################################
        ###  Notas:  ##############################################################################
        ###  -También incluyo Params_Xmass_species en fastchem porque cuando tenga aerosoles  #####
        ###  alomejor tendré que meter los datos del fichero, fastchem no tiene aerosoles  ########
        ###  -se llama a la fcn names2names... para cambiar a notación fastchem  ##################
        ###  -pyfastchem es un módulo, no una función dentro de las subcarpetas del tfm   #########
        ###  -Se añaden directorios necesarios para fastchem  #####################################
        ###  -la carpeta dir_fastchem_element_abundances tiene abundancias de elementos químicos ##
        ###  -la carpeta dir_fastchem_log_k tiene los coeficientes de ajuste para las cte de  #####
        ###  equilibrio  ##########################################################################
        ###  -el objeto fastchem se guarda en la variable fastchem   ##############################
        ###  -FastChemInput() y FastChemOutput() sirven para configurar entradas y salidas de  ####
        ###  fastchem; las variables input_data y output_data crean instancias de entrada y  ######
        ###  salida  ##############################################################################
        ###  -temperatures_guillot_K se calcula a partir de la función temperature_profile_func- ##
        ###  tion_guillot_global. Esta utiliza: gamma: ratio entre la opacidad en óptico e IR, ####
        ###  T_int_K: temperatura interna, T_equ_K: temperatura de equilibrio, kappa_IR: opacidad #
        ###  en IR. ###############################################################################
        ###  -Con la función calcDensities calculo las densidades químicas A PARTIR DEL OBJETO  ###
        ###  fastchem que he creado previamente  ##################################################
        ###  -la variable species_indices_fastchem guarda los índices que utiliza fastchem ########
        ###  asociados a cada especie A PARTIR DE SU NOTACIÓN FASTCHEM (species_labels_fastchem) ##
        ###########################################################################################

    elif modo == 'fastchem':
        
        params_Xmass_species = None
        
        ###########################################################################################
        ######  FastChem  #########################################################################
        ###########################################################################################
        ###  Notas:  ##############################################################################
        ###  - En este modo se usa FastChem para obtener la composición en equilibrio químico.   ###
        ###  - Se asume una mezcla química inicial basada en abundancias solares (Asplund 2009). ###
        ###  - No se imponen fracciones en masa de especies, FastChem calcula todas las posibles.###
        ###  - Posteriormente se seleccionan las especies relevantes para petitRADTRANS.         ###
        ###########################################################################################

        import pyfastchem 

        # Rutas a ficheros de entrada
        dir_fastchem_element_abundances = os.path.join(dir_main, "..", "MODELOS", "FastChem", "input", "element_abundances")
        path_fastchem_element_abundances = os.path.join(dir_fastchem_element_abundances, "asplund_2009.dat")
        dir_fastchem_logK = os.path.join(dir_main, "..", "MODELOS", "FastChem", "input", "logK")
        path_fastchem_logK = os.path.join(dir_fastchem_logK, "logK.dat")

        # Inicializo FastChem
        fastchem = pyfastchem.FastChem(path_fastchem_element_abundances, path_fastchem_logK, 1)

        # Creo estructuras de entrada/salida
        input_data = pyfastchem.FastChemInput()
        output_data = pyfastchem.FastChemOutput()
        #print(len(params_basic.temperatures_K), len(params_basic.pressures_bar))

        # Asigno perfil de presión y temperatura
        input_data.temperature = params_basic.temperatures_K
        input_data.pressure = params_basic.pressures_bar

        # Ejecuto FastChem
        fastchem_flag = fastchem.calcDensities(input_data, output_data)

        if np.amin(output_data.element_conserved[:]) == 1:
            print("Conservación de elementos: OK")
        else:
            print("Conservación de elementos: FALLIDA")

        species_labels_fastchem = ["C1O1", "C1O2", "N2", "C1H4", "H1O2", "O2"]

        # Obtienes los índices para cada especie usando fastchem.getGasSpeciesIndex y creas un diccionario
        species_to_index = {species: fastchem.getGasSpeciesIndex(species) for species in species_labels_fastchem}

        #print(species_to_index)
        number_densities_molec_m3 = np.array(output_data.number_densities)

        gas_number_density_molec_m3 = params_basic.pressures_bar * 1e6 / (cst.kB * params_basic.temperatures_K)

        Params_fastchem = namedtuple("Params_fastchem", "species_to_index, number_densities_molec_m3, gas_number_density_molec_m3")
        params_fastchem = Params_fastchem(
            species_to_index = species_to_index,
            number_densities_molec_m3 = number_densities_molec_m3,
            gas_number_density_molec_m3 = gas_number_density_molec_m3
        )
        #print(len(output_data.number_densities), len(params_basic.pressures_bar))

        print(f'Se seleccionaron las especies para análisis espectral: {species_labels_fastchem}')

        return None, params_fastchem



