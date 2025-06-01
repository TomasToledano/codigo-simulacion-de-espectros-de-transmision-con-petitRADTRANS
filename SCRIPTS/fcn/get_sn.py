###########################################################################################
###########################################################################################
###  -Se importan las librerias necesarias  ###############################################
###  -Se importan las estructuras params_ben1_fichero y params_ben1_noCO2_fichero para  ###
###  para extraer la profundidad de tránsito con y sin CO2 en función de la longitud de ###
###  onda. Estos parámetros son necesarios para calcular la S/N  ##########################
###########################################################################################
###########################################################################################

import os
import sys

dir_fcn = os.getcwd()
dir_main = os.path.join(dir_fcn, "..")

sys.path.append(dir_main)

from config import np, fits, plt, ticker, math
from get_output_params import params_ben1_fichero, params_ben1_noCO2_fichero

##########################################################################################
###  -Se lee el archivo fits descargado de ETC para extraer la sn de la estrella  ########
###  -Si el archivo se llama lineplot_sn_4_40_2_59.fits significa que: grupos por ########
###  integración = 4, integraciones por exposición = 40, dithers = 2 y tiempo total por ##
###  exposición = 59  ####################################################################
##########################################################################################
##########################################################################################

dir_data_input = os.path.join(dir_main, "..", "data_input")
#path_archivo_ETC = os.path.join(dir_data_input, 'lineplot_sn_4_40_2_59.fits')
path_archivo_ETC = os.path.join(dir_data_input, 'lineplot_sn_2_120_2_108.fits')

with fits.open(path_archivo_ETC) as hdul:
    tabla = hdul[1].data
    wavelength_um = tabla['WAVELENGTH']  
    sn_star = tabla['sn']

sn_star = np.nan_to_num(sn_star, nan=0.0)

##########################################################################################
###  -Se interpolan las profundidades de tránsito en el rango de longitud de onda que  ###
###  tiene el achivo fits del ETC correspondiente al rango que cubre el detector NIRSPEC #
###  -Se calcula la diferencia 'delta' entre ambos espectros  ############################
###  -Se grafican ambos espectros y la delta  ############################################
##########################################################################################
##########################################################################################

wavelength_um_CO2 = params_ben1_fichero.wavelengths_cm * 1e4  
depth_ppm_CO2 = params_ben1_fichero.depth_ppm

wavelength_um_noCO2 = params_ben1_noCO2_fichero.wavelengths_cm * 1e4  
depth_ppm_noCO2 = params_ben1_noCO2_fichero.depth_ppm

depth_interp_CO2 = np.interp(wavelength_um, wavelength_um_CO2, depth_ppm_CO2)
depth_interp_noCO2 = np.interp(wavelength_um, wavelength_um_noCO2, depth_ppm_noCO2)

delta_depth_ppm = depth_interp_CO2 - depth_interp_noCO2

plt.figure(figsize=(10, 6))
plt.plot(wavelength_um, depth_interp_CO2, label='Con CO2', color='red', linewidth=2)
plt.plot(wavelength_um, depth_interp_noCO2, label='Sin CO2', color='b', linestyle='-.', linewidth=2)
plt.plot(wavelength_um, delta_depth_ppm, label='Delta', color='green', linestyle='-')

plt.minorticks_on()
plt.xlabel('Longitud de onda (μm)', fontsize=18)
plt.ylabel('Profundidad de tránsito (ppm)', fontsize=18)
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(4)) 
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

##########################################################################################
###  -Se calcula la S/N del planeta para una exposición a cada longitud de onda para  ####
###  las lineas de CO2  ##################################################################
###  -Se grafican la S/N de la estrella, la delta_depth_ppm y S/N del planeta para una  ##
###  exposición  ######################################################################### 
##########################################################################################
##########################################################################################
 
sn_planet = sn_star * (delta_depth_ppm * 1e-6) / np.sqrt(2)

fig, ax1 = plt.subplots(figsize=(10, 6))
color1 = 'tab:blue'
ax1.set_xlabel('Longitud de onda (μm)', fontsize=18)
ax1.set_ylabel('S/N$_{\mathrm{estrella}}$', color=color1, fontsize=18)
ax1.plot(wavelength_um, sn_star, color=color1, label='S/N estrella')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.minorticks_on()
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(4)) 
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)

ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('Δ profundidad de tránsito (ppm)', color=color2, fontsize=18)
ax2.plot(wavelength_um, delta_depth_ppm, color=color2, linestyle='--', label='Δ depth')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.minorticks_on()
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(4)) 
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='minor', labelsize=10)

ax3 = ax1.twinx()
color3 = 'tab:green'
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('S/N$_{\mathrm{planeta}}$', color=color3, fontsize=18)
ax3.plot(wavelength_um, sn_planet, color=color3, linestyle='-.', label='S/N CO2')
ax3.tick_params(axis='y', labelcolor=color3)
ax3.minorticks_on()
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(4)) 
ax3.tick_params(axis='both', which='major', labelsize=12)
ax3.tick_params(axis='both', which='minor', labelsize=10)

fig.tight_layout()
plt.show()

##########################################################################################
###  -Se calcula la S/N del planeta total sumando cuadráticamente la S/N a cada longitud #
###  de onda y teniendo en cuenta la duración del tránsito  ##############################
##########################################################################################
##########################################################################################

sn_planet_total = np.sqrt(np.sum(sn_planet**2))

sn_1 = sn_planet_total * np.sqrt(3345 / 108)
print(f"La S/N en 1 tránsito es: {sn_1:.2f}")

sn_4 = sn_1 * np.sqrt(4)
print(f"La S/N en 4 tránsitos es: {sn_4:.2f}")

N_t_5sigmas = (5 / sn_1) ** 2
print(f"El número de tránsitos necesarios para detección de 5 sigmas es: {math.ceil(N_t_5sigmas)}")


