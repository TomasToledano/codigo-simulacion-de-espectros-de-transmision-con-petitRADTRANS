from petitRADTRANS.planet import Planet

planet = Planet.get('TRAPPIST-1 e')

def get_planet_property(property_name):
    """
    Obtiene una propiedad específica del planeta TRAPPIST-1 e usando petitRADTRANS.

    Args:
        property_name (str): La propiedad que deseas consultar.

    Returns:
        str: El valor de la propiedad, o un mensaje de error si no existe.
    """
    try:
        # Fijar el nombre del planeta como 'TRAPPIST-1 e'
        planet_name = 'TRAPPIST-1 e'
        
        # Obtener el objeto del planeta
        planet = Planet.get(planet_name)
        
        # Verificar si la propiedad existe en el objeto del planeta
        if hasattr(planet, property_name):
            property_value = getattr(planet, property_name)
            return f"{planet_name}'s {property_name}: {property_value}"
        else:
            return f"La propiedad '{property_name}' no existe para el planeta {planet_name}."
    except Exception as e:
        return f"Error al obtener datos del planeta '{planet_name}': {e}"

property_name = 'orbit_semi_major_axis'

star_rad = 'reference_gravity'

print(get_planet_property(property_name))
print(get_planet_property(star_rad))

print(get_planet_property('units'))



for key in planet.__dict__:
    print(f"{key}")
