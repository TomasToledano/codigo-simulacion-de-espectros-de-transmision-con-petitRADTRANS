from config import plt

def get_pt_profile(params_basic):
    plt.plot(params_basic.temperatures_K, params_basic.pressures_bar)
    plt.gca().invert_yaxis()
    plt.xlabel('T (K)')
    plt.ylabel('P (bar)')
    plt.yscale('log')

    plt.show()

