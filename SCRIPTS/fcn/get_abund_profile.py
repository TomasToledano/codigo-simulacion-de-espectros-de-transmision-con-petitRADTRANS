from config import plt, ticker

def get_abund_profile(params_basic, mass_fractions):
    pressures_hpa = params_basic.pressures_bar * 1000  # Convertir de bar a hPa

    fig, ax = plt.subplots(figsize=(8, 6))  # Crear figura y ejes fuera del bucle

    for species, fraction in mass_fractions.items():
        if species == 'H2O(s)_crystalline__Mie':
            label = 'H2O(s)'
        else:
            label = species
        ax.plot(fraction, pressures_hpa, label=label)

    ax.invert_yaxis()
    ax.set_xlabel('Fracción de masa', fontsize=18)
    ax.set_ylabel('Presión (hPa)', fontsize=18)
    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.ticklabel_format(style='plain', axis='y')
    ax.legend(fontsize=18)
    plt.tight_layout()
    plt.savefig('dasd.png')
    plt.show()

