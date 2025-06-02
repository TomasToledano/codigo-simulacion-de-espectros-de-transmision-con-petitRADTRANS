
###########################################################################################
###########################################################################################
###  Se importan los paquetes y funciones necesarios y se nombran los directorios #########
###########################################################################################
###########################################################################################
###########################################################################################

from config import os, sys, np, plt, ticker
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import LogFormatter, FixedLocator
plt.rcParams['text.usetex'] = False

dir_main = os.getcwd()  
dir_funciones = os.path.join(dir_main, "fcn")

sys.path.append(dir_funciones)

from get_params import get_params
from get_output_params import params_ben1_fichero, params_ben1_fastchem, params_ben2_fichero, params_ben2_fastchem, params_ben1_noCO2_fichero, params_ben1_noCIA_fichero, params_ben2_noCIA_fichero, params_hab1_fichero_05micras, params_hab1_fichero_14micras, params_hab1_fichero_50micras

###########################################################################################
###########################################################################################
###  Selección de caso y modo  ############################################################
###########################################################################################
###########################################################################################
###########################################################################################

caso = 'ben1'
#caso = 'ben2'
modo = 'fichero'
#modo = 'fastchem'

###########################################################################################
###########################################################################################
###  Se importan las estructuras igual que en el main por para tener también aquí  ########
###  los parámetros  ######################################################################
###########################################################################################
###########################################################################################
###########################################################################################

params_planet, params_basic = get_params(dir_main, caso)
dir_figures = os.path.join(dir_main, "figures", f"{params_basic.case_label}")



#params_caso_modo = globals()[f'params_{params_basic.case_label}_{modo}']

##########################################################################################
#####  Función para graficar diagramas presión-temperatura  ##############################
##########################################################################################

def plot_pressure_temperature(params_basic, dir_figures):
    """
    Genera un diagrama Presión-Temperatura.
    
    Args: params_basic se usa para introducir la variable case_label y dar nombre a las gráficas de salida
    """
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Graficar los datos
    ax.plot(params_caso_modo.temperatures_K, params_caso_modo.pressures_bar* 1e3, label={params_basic.case_label})
    #ax.plot(params_caso_modo.temperatures_K, params_caso_modo.pressures_bar * 1e3, label='Ben1', linewidth=2)

    #ax.plot(params_ben2_fichero.temperatures_K, params_ben2_fichero.pressures_bar * 1e3, label='Ben2', linewidth=2)
    
    # Configurar ejes
    ax.set_xlabel("Temperatura (K)", fontsize=18)
    ax.set_ylabel("Presión (hPa)", fontsize=18)
    ax.set_yscale('log')
    ax.invert_yaxis()

    # Forzar etiquetas "0.1", "1", "10" en el eje Y
    yticks = [0.1, 1, 10, 100, 1000]  # ajusta según tu rango
    ax.set_yticks(yticks)
    ax.get_yaxis().set_major_formatter(LogFormatter(labelOnlyBase=False))
    
    # Configurar ticks
    ax.minorticks_on()
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.tick_params(axis='both', which='minor', labelsize=10)
    
    # Leyenda y guardado
    #ax.legend(fontsize=20)
    plt.savefig(f"{dir_figures}/presion_temperatura_{params_basic.case_label}.png")
    plt.show()

#plot_pressure_temperature(params_basic, dir_figures)


##########################################################################################
#####  Función para graficar diagramas presión-abundancia  ###############################
##########################################################################################

def plot_pressure_abundances(params_basic, dir_figures, modo):
    """
    Genera un gráfico de Presión-Abundancias químicas.
    
    Args: params_basic y modo se usa para introducir la variable case_label y dar nombre a las gráficas de salida

    """
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Graficar las abundancias
    for species, abundance in [("N2", params_caso_modo.mass_fraction_N2), ("CO2", params_caso_modo.mass_fraction_CO2), ("H2O_l", params_caso_modo.mass_fraction_H2O_l), ("H2O_s", params_caso_modo.mass_fraction_H2O_s)]:
        ax.plot(abundance, params_caso_modo.pressures_bar, label=f"{species}")
    
    # Configurar ejes
    ax.set_xlabel("Fracción en masa", fontsize=18)
    ax.set_ylabel("Presión (bar)", fontsize=18)
    ax.invert_yaxis()
    plt.yscale('log')
    plt.xscale('log')

    # Configurar ticks
    ax.minorticks_on()
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.tick_params(axis='both', which='minor', labelsize=10)
    
    # Leyenda y guardado
    ax.legend(fontsize=16)
    #plt.savefig(f"{dir_figures}/presion_abundancia_{params_basic.case_label}_{modo}.png")
    plt.show()

#plot_pressure_abundances(params_basic, dir_figures, modo)


##########################################################################################
#####  Función para graficar diagramas Radio de Tránsito vs Longitud de onda  ############
##########################################################################################



def plot_transit_radius(dir_figures, params_basic, modo):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.plot(params_ben1_fichero.wavelengths_cm * 1e4, params_ben1_fichero.depth_ppm, color='blue', linestyle='--' , linewidth=1, label='Ben1')
    # Graficar el espectro en ppm (eje izquierdo)
    ax1.plot(params_hab1_fichero_05micras.wavelengths_cm * 1e4, params_hab1_fichero_05micras.depth_ppm, color='deeppink', linewidth=2.5, label=r'$R_{\mathrm{partícula}}$ H$_{\mathrm{2}}$O(s): 0.5 $\mu$m')
    ax1.plot(params_hab1_fichero_14micras.wavelengths_cm * 1e4, params_hab1_fichero_14micras.depth_ppm, color='purple', linestyle='-' ,linewidth=2, label=r'$R_{\mathrm{partícula}}$ H$_{\mathrm{2}}$O(s): 14 $\mu$m')
    ax1.plot(params_hab1_fichero_50micras.wavelengths_cm * 1e4, params_hab1_fichero_50micras.depth_ppm, color='gray', linestyle='-' , linewidth=1.5, label=r'$R_{\mathrm{partícula}}$ H$_{\mathrm{2}}$O(s): 50 $\mu$m')


    
    # Crear un segundo eje y (derecha) para altura en km
    ax2 = ax1.twinx()

    # Calcular altura en km
    altura_km = (params_hab1_fichero_05micras.radio_transito_cm - params_planet.planet_radius_cm) / 1e5
    ax2.plot(params_hab1_fichero_05micras.wavelengths_cm * 1e4, altura_km, alpha=0)

    # Configurar ejes
    ax1.set_xlabel("Longitud de onda (μm)", fontsize=18)
    ax1.set_ylabel("Profundidad de tránsito (ppm)", fontsize=18)
    ax2.set_ylabel('Altura (km)', fontsize=18)
    ax1.set_xscale('log')
    ax1.set_xlim(0.6, 50)

    # Ajustar el máximo de ppm y desplazar el mínimo para que no empiece en cero
    ppm_min = min(params_hab1_fichero_05micras.depth_ppm) - 3  # Desplazamos el mínimo para empezar en -3
    ppm_max = max(params_hab1_fichero_05micras.depth_ppm) * 1.15
    ax1.set_ylim(ppm_min, ppm_max)

    # Ajustar el eje derecho para que coincida visualmente con el eje izquierdo
    factor_min = (ppm_min / 5012) + 1
    factor_max = (ppm_max / 5012) + 1
    r_t_min = params_planet.planet_radius_cm * np.sqrt(factor_min)
    r_t_max = params_planet.planet_radius_cm * np.sqrt(factor_max)
    alt_min_km = (r_t_min - params_planet.planet_radius_cm) / 1e5
    alt_max_km = (r_t_max - params_planet.planet_radius_cm) / 1e5
    ax2.set_ylim(alt_min_km, alt_max_km)

    # Añadir ticks personalizados
    #ax1.set_yticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])  # Para ppm
    ax1.set_yticks([0, 20, 40, 60, 80])  # Para ppm

    ax2.set_yticks([0, 20, 40])  # Para altura en km, asegurar que 50 km esté incluido

    # Establecer los ticks y sus labels (usamos los mismos valores para ticks y labels)
    ticks = [0.6, 1, 1.4, 2, 3, 4, 5, 7,  10, 13, 16, 20, 30, 40, 50]
    #ticks = [0.6, 1, 1.4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
    plt.xticks(ticks, labels=[str(val) for val in ticks])

    # Formato de ticks
    ax1.minorticks_on()
    ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    ax2.yaxis.set_major_locator(MultipleLocator(10))
    ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))

    ax1.tick_params(axis='y', which='major', labelsize=14)
    ax1.tick_params(axis='x', which='major', labelsize=13)
    ax1.tick_params(axis='both', which='minor', labelsize=10)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax2.tick_params(axis='both', which='minor', labelsize=10)

    # Generar el nombre del archivo
    filename = f"{dir_figures}/transit_radius_{params_basic.case_label}_{modo}.png"
    
    # Comprobar si el archivo ya existe, y si es así, generar un nombre único
    if os.path.exists(filename):
        base, ext = os.path.splitext(filename)
        i = 1
        # Mientras exista el archivo, incrementar el sufijo
        while os.path.exists(f"{base}_{i}{ext}"):
            i += 1
        filename = f"{base}_{i}{ext}"

    # Guardar y mostrar la figura
    ax1.legend(fontsize=14, loc='upper left')
    plt.savefig(filename)
    plt.show()


plot_transit_radius(dir_figures, params_basic, modo)

