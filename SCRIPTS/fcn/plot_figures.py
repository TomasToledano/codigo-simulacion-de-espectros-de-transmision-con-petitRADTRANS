from config import os, plt, np, LogLocator, MultipleLocator

def plot_figures(x_data, y_data, dir_figures, caso, modo, params_basic, xlabel='Wavelength [microns]', 
                  ylabel=r'Transit radius [$\rm R_{Jup}$]', xscale='log', 
                  figsize=(10, 6), label=None):
    """
    Genera una figura preliminar para visulaizar los espectros, no es para generar figuras enriquecidas.
    
    Notas:
    - species_labels: Lista de elementos utilizados
    - label: Etiqueta para la leyenda (opcional)
    """
    species_labels_string = "_".join(params_basic.species_labels)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(x_data, y_data, label=label)
    ax.set_xscale(xscale)
    
    if label:
        ax.legend()
        
    ax.minorticks_on()

    # Defino los ticks en el eje x
    ticks = [0.6, 1, 1.4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]
    #ticks = [0.6, 1, 1.4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 35, 50]

    # Se establecen los ticks y sus labels (mismos valores para ticks y labels)
    plt.xticks(ticks, labels=[str(val) for val in ticks])
     
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.set_xlabel(xlabel, fontsize = 14)
    ax.set_ylabel(ylabel, fontsize = 14)
    plt.xlim(0.6, 20)
    plt.ylim(0, 100)
    plt.show()
