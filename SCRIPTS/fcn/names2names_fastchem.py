###########################################################################################
###########################################################################################
###  import re  ###########################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###  Notas:  ##############################################################################
###  Es una importación del módulo de Python que significa "expresiones regulares". Este ##
###  módulo proporciona herramientas para trabajar con expresiones regulares, que son #####
###  secuencias de caracteres que definen un patrón de búsqueda.  #########################
###########################################################################################
###########################################################################################
###########################################################################################

import re

def names2names_fastchem(specie):
    """
    Transforma una especie en notación "normal" a notación fastchem.

    Args: especie en notación normal

    Return: especie en notación fastchem

    """
    ####NO VALE PARA TODOS LOS ELEMENTOS DE FASTCHEM PERO SÍ PARA LA MAYORÍA Y PARA TODOS LOS QUE SE VAN A UTILIZAR EN EL TRABAJO####
    
    #####################################################################################
    #####  names2names_fastchem  ########################################################
    #####################################################################################
    ###  Notas:  ########################################################################
    ###  -[A-Z] es para ver la letra mayúscula que puede ir seguida O NO de una minús- ##
    ###  cula (para esto se pone el asterisco depues de la letra minúscula [a-z]* indi- #
    ###  cando que puede haber o no minúscula.  #########################################
    ###  -\d es para designar un número entre: [0-9], se vuelve a poner * por si no hay #
    ###  número.  #######################################################################
    ###  -la variables h_elements es para almacenar los elementos que contienen 'H' #####
    ###  -la variables c_elements es para almacenar los elementos que contienen 'C' #####
    ###  -se añaden a names_fastchem en el orden C, H, otros, para que cumplan los  #####
    ###  criterios de fastchem ##########################################################
    ###  -se guarda en elements_no_one los elementos que no deben llevar 1  #############
    #####################################################################################

    elements_no_one = {'He', 'K', 'Na', 'H', 'Ne', 'Ar', 'Al', 'Ca', 'Mg', 'Mn', 'Ni', 'O', 'F', 'P', 'S', 'Si', 'Ti', 'V', 'Cr', 'Cu', 'Zn', 'Fe', 'Ge'}
        
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', specie) 
   
    names_fastchem = ''
    h_elements = []  
    c_elements = []  
    other_elements = [] 

    for element, numero in elements:
        if numero == '' and element in elements_no_one:
            numero = ''  
        elif numero == '':  
            numero = '1'

        if element == 'O':
            if numero == '':
                numero = '1'
        
        if element == 'C':
            c_elements.append(f"{element}{numero}")
            
        elif element == 'H':
            h_elements.append(f"{element}{numero}")
        
        else:
            other_elements.append(f"{element}{numero}")

    names_fastchem += ''.join(c_elements)
    names_fastchem += ''.join(h_elements)
    names_fastchem += ''.join(other_elements)
    
    return names_fastchem


