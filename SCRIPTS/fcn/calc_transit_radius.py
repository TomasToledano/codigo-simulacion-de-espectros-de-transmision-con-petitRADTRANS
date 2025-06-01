from config import utils, np, cst, plt

def calc_transit_radius(modo, aerosol, mass_fractions, atmosphere, params_basic, params_planet):
    """
    Calcula el radio de tránsito a partir del objeto prt guardado en atmosphere usando la función calculate_transit_radii de prt.

    Args: params_basic, params_planet, params_prt, mass_fractions, atmosphere

    Return: Devuelve la longitud de onda en amstrongs y el radio de tránsito en cm
    """

      
    #calculo la mean molar mass ahora, antes la tenia en get params pero cambia si es fastchem o fichero asi aqui mejor
    mean_molar_masses = utils.compute_mean_molar_masses(mass_fractions)
    print(mean_molar_masses)
    
    if aerosol == 'no':

        wavelengths_cm, radio_transito_cm, _ = atmosphere.calculate_transit_radii(
            temperatures = params_basic.temperatures_K,
            mass_fractions = mass_fractions,
            mean_molar_masses = mean_molar_masses,
            reference_gravity = params_planet.reference_gravity_cgs,
            planet_radius = params_planet.planet_radius_cm,
            reference_pressure = params_planet.reference_pressure_bar,
            return_contribution=False
            )
        
        delta_ppm = 5012
               
        depth_ppm = np.array(delta_ppm * ((radio_transito_cm**2 / params_planet.planet_radius_cm**2) - 1))

        return wavelengths_cm, radio_transito_cm, depth_ppm

    elif aerosol == 'si':
        
        cloud_particles_mean_radii = {'H2O(l)':  (1.4e-3) * np.ones_like(params_basic.temperatures_K), 'H2O(s)_crystalline__Mie': (1.0e-5) * np.ones_like(params_basic.temperatures_K)}

        cloud_particle_radius_distribution_std = 1.05

        wavelengths_cm, radio_transito_cm, _ = atmosphere.calculate_transit_radii(
            temperatures = params_basic.temperatures_K,
            mass_fractions = mass_fractions,
            mean_molar_masses = mean_molar_masses,
            reference_gravity = params_planet.reference_gravity_cgs,
            planet_radius = params_planet.planet_radius_cm,
            reference_pressure = params_planet.reference_pressure_bar,
            cloud_particles_mean_radii = cloud_particles_mean_radii,
            cloud_particle_radius_distribution_std = cloud_particle_radius_distribution_std
            )

        delta_ppm = 5012
               
        depth_ppm = np.array(delta_ppm * ((radio_transito_cm**2 / params_planet.planet_radius_cm**2) - 1))

        return wavelengths_cm, radio_transito_cm, depth_ppm




