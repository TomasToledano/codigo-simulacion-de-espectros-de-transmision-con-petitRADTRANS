from config import os, np, namedtuple

dir_actual = os.path.dirname(os.path.abspath(__file__))

dir_funciones = dir_actual

dir_data_output_ben1 = os.path.join(dir_funciones, "..", "output_data", "ben1")
dir_data_output_ben2 = os.path.join(dir_funciones, "..", "output_data", "ben2")
dir_data_output_hab1 = os.path.join(dir_funciones, "..", "output_data", "hab1")

##########################################################################################
##########################################################################################
###  ben1  ###############################################################################
##########################################################################################
##########################################################################################
##########################################################################################

##############################################
###  Fichero  ################################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_fichero_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_fichero_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben1_fichero = namedtuple("Params_ben1_fichero", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben1_fichero = Params_ben1_fichero(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )

##############################################
###  Fichero sin choques N2-N2 (sin CIAs)  ###
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_noCIA_fichero_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_noCIA_fichero_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben1_noCIA_fichero = namedtuple("Params_ben1_noCIA_fichero", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben1_noCIA_fichero = Params_ben1_noCIA_fichero(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )

##############################################
###  Fichero sin CO2 para S/N  ###############
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_noCO2_fichero_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_noCO2_fichero_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben1_noCO2_fichero = namedtuple("Params_ben1_noCO2_fichero", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben1_noCO2_fichero = Params_ben1_noCO2_fichero(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )

##############################################
###  Fastchem  ###############################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_fastchem_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben1, "output_data_ben1_fastchem_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben1_fastchem = namedtuple("Params_ben1_fastchem", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben1_fastchem = Params_ben1_fastchem(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm    
    )

##########################################################################################
##########################################################################################
###  ben2  ###############################################################################
##########################################################################################
##########################################################################################
##########################################################################################

##############################################
###  Fichero  ################################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben2, "output_data_ben2_fichero_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben2, "output_data_ben2_fichero_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben2_fichero = namedtuple("Params_ben2_fichero", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben2_fichero = Params_ben2_fichero(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )

##############################################
###  Fichero sin choques N2-N2  ##############
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben2, "output_data_ben2_noCIA_fichero_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben2, "output_data_ben2_noCIA_fichero_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben2_noCIA_fichero = namedtuple("Params_ben2_noCIA_fichero", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben2_noCIA_fichero = Params_ben2_noCIA_fichero(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )

##############################################
###  Fastchem  ###############################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2 = np.loadtxt((os.path.join(dir_data_output_ben2, "output_data_ben2_fastchem_atm.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_ben2, "output_data_ben2_fastchem_spectrum.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))

Params_ben2_fastchem = namedtuple("Params_ben2_fastchem", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 wavelengths_cm radio_transito_cm depth_ppm")

params_ben2_fastchem = Params_ben2_fastchem(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )

##########################################################################################
##########################################################################################
###  hab1  ###############################################################################
##########################################################################################
##########################################################################################
##########################################################################################

##############################################
###  Fichero  ################################
##############################################
###  0.5 micras  #############################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2, mass_fraction_H2O_l, mass_fraction_H2O_s = np.loadtxt((os.path.join(dir_data_output_hab1, "output_data_hab1_fichero_atm_05micras.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_hab1, "output_data_hab1_fichero_spectrum_05micras.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))


Params_hab1_fichero_05micras = namedtuple("Params_hab1_fichero_05micras", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 mass_fraction_H2O_l mass_fraction_H2O_s wavelengths_cm radio_transito_cm depth_ppm")

params_hab1_fichero_05micras = Params_hab1_fichero_05micras(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    mass_fraction_H2O_l = mass_fraction_H2O_l,
    mass_fraction_H2O_s = mass_fraction_H2O_s,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )


##############################################
###  Fichero  ################################
##############################################
###  14 micras  ##############################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2, mass_fraction_H2O_l, mass_fraction_H2O_s = np.loadtxt((os.path.join(dir_data_output_hab1, "output_data_hab1_fichero_atm_14micras.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_hab1, "output_data_hab1_fichero_spectrum_14micras.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))


Params_hab1_fichero_14micras = namedtuple("Params_hab1_fichero_14micras", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 mass_fraction_H2O_l mass_fraction_H2O_s wavelengths_cm radio_transito_cm depth_ppm")

params_hab1_fichero_14micras = Params_hab1_fichero_14micras(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    mass_fraction_H2O_l = mass_fraction_H2O_l,
    mass_fraction_H2O_s = mass_fraction_H2O_s,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )


##############################################
###  Fichero  ################################
##############################################
###  50 micras  ##############################
##############################################

temperatures_K, pressures_bar, z_km, mass_fraction_N2, mass_fraction_CO2, mass_fraction_H2O_l, mass_fraction_H2O_s = np.loadtxt((os.path.join(dir_data_output_hab1, "output_data_hab1_fichero_atm_50micras.txt")), unpack = True, skiprows = 1, usecols = (0,1,2,3,4,5,6))
wavelengths_cm, radio_transito_cm, depth_ppm = np.loadtxt((os.path.join(dir_data_output_hab1, "output_data_hab1_fichero_spectrum_50micras.txt")), unpack = True, skiprows = 1, usecols = (0,1,2))


Params_hab1_fichero_50micras = namedtuple("Params_hab1_fichero_50micras", "temperatures_K pressures_bar z_km mass_fraction_N2 mass_fraction_CO2 mass_fraction_H2O_l mass_fraction_H2O_s wavelengths_cm radio_transito_cm depth_ppm")

params_hab1_fichero_50micras = Params_hab1_fichero_50micras(
    temperatures_K = temperatures_K,
    pressures_bar = pressures_bar,
    z_km = z_km,
    mass_fraction_N2 = mass_fraction_N2,
    mass_fraction_CO2 = mass_fraction_CO2,
    mass_fraction_H2O_l = mass_fraction_H2O_l,
    mass_fraction_H2O_s = mass_fraction_H2O_s,
    wavelengths_cm = wavelengths_cm,
    radio_transito_cm = radio_transito_cm,
    depth_ppm = depth_ppm
    )
