import os
import sys
import numpy as np

dir_funciones = os.getcwd()  
dir_fastchem_element_abundances = os.path.join(dir_funciones, "..", "..", "MODELOS", "FastChem", "input", "element_abundances")
path_fastchem_element_abundances = os.path.join(dir_fastchem_element_abundances, "asplund_2020.dat")




data = np.loadtxt(path_fastchem_element_abundances, dtype=str, comments='#')

elementos = data[:, 0]  
abundancias = data[:, 1].astype(float)  

print("Elementos:", elementos)
print("Abundancias:", abundancias)
