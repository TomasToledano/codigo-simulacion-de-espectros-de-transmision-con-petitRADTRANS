
====================
#**Código de espectros de transmisión para desarrollo del TFM: Simulación de espectros de transmisión de atmósferas de planetas rocosos**

**Autor**: Tomás Toledano Mazarío (tomastol@ucm.es)  
====================



> Descripción general
====================
Este repositorio contiene scripts en Python para generar espectros de transmisión exoplanetarios utilizando el código de transporte radiativo petitRADTRANS. También se utiliza FastChem para los cálculos de equilibrio químico. El código está diseñado como una herramienta para facilitar el modelado atmosférico en investigación de exoplanetas.
====================



> Estructura principal del repositorio
===================
.
├── data_input/				# Archivos de datos de entrada
│   ├── lineplot_sn_2_120_2_108.fits    # Archivo FITS extraidos de la Calculadora de Tiempo de exposición del JWST
│   ├── lineplot_sn_4_40_2_59.fits      # Archivo FITS extraidos de la Calculadora de Tiempo de exposición del JWST
│   └── vertical_profiles_termin_avg_*  # Perfiles verticales atmosféricos de cada escenario (Ben1, Ben2, Hab)
│   └── Nota: Aquí se genera la carpeta con las tablas de opacidades automaticamente la primera vez que se ejecuta el código.
│
├── MODELOS/				# Modelos utilizados en el trabajo
│   ├── FastChem/                 	# Carpeta con FastChem (mirar (4) para su instalación)
│   └── petitRADTRANS/            	# Carpeta con petitRADTRANS (mirar (3) para su instalación)
│
├── SCRIPTS/			        # Scripts principales de Python
│   ├── fcn/                            # Funciones 
│   ├── figures/            	        # Figuras generadas con plot_master.py
│   ├── output_data/            	# Datos de salida para generar gráficos con la función plot_master.py
│   ├── config.py                 	# Script para sintetizar las importaciones de librerias
│   ├── main.py                   	# Script principal
│   └── plot_master.py            	# Script maestro para generar gráficos enriquecidos
│
└── README.md				# Este archivo 
====================



> Instalar dependencias y modelos
====================
1) descargar dependencias:
	> Las dependencias como numpy y matplotlib se instalan automaticamente al instalar petitRADTRANS (paso 3). NOTA: prt te cambia numpy a una versión inferior.
	>> sudo dnf install python3 python3-pip gcc-gfortran chromium 
	#gcc-gfortran es necesario para compilar las opacidades y módulos numéricos de pRT.

2) crear directorio MODELOS, TIENE QUE ESTAR DENTRO DE LA 'carpeta_principal' que contenga todas las carpetas SIGUIENDO LA JERARQUÍA previamente mostrada en 'Estructura del repositorio'.
	-> dentro de MODELOS tendré dos carpetas que se crearán al instalar los modelos: FastChem, petitRADTRANS
	
	
3) instalacion de petitRADTRANS
	1) git clone https://gitlab.com/mauricemolli/petitRADTRANS.git  	# Dentro de la carpeta MODELOS instalo petitradtrans, es posible que pida antes instalar git-core
	2) cd petitRADTRANS/ 							# Me meto en la carpeta que se ha creado
	3) pip install . 							# Dentro de la carpeta utilizo '>>pip install .' para instalar el paquete petitRADTRANS en python; es posible que de error y haya que usar comandos como: >>sudo dnf install python3-devel   >>sudo dnf install pkg-config

4) instalacion de fastchem
	1) sudo dnf install cmake						# Instalo cmake, necesario para compilar proyectos como Fastchem
	2) cmake --version  							# Comprobar instalación
	
	3) git clone --depth 1 https://github.com/NewStrangeWorlds/FastChem 	# Dentro de la carpeta MODELOS instalo fastchem
	4) cd FastChem/  							# Me meto en la carpeta que se ha creado
	5) mkdir build && cd build  						# Creo carpeta para compilar FastChem, ya que está escrito en C++
	6) cmake ..
	7) pip install pyfastchem						#instalar librería
====================



> Referencias
====================
Mollière, P., Wardenier, J. P., van Boekel, R., Henning, T., Molaverdikhani, K., & Snellen, I. A. G. (2019). *petitRADTRANS: A Python radiative transfer package for exoplanet characterization*. Astronomy & Astrophysics, 627, A67.  
https://doi.org/10.1051/0004-6361/201834696

Stock, J. W., Kitzmann, D., Patzer, A. B. C., & Sedlmayr, E. (2018). *FastChem: A computer program for efficient coupling of gas-phase chemical kinetics and thermodynamics*. Monthly Notices of the Royal Astronomical Society, 479(1), 865-874.  
https://doi.org/10.1093/mnras/sty1411

Space Telescope Science Institute. (2025). *JWST Exposure Time Calculator* (Version 4.1) [Web application]. 
https://jwst.etc.stsci.edu/

Guía con instalación, tutorial y fragmentos de código de petitRADTRANS:	https://petitradtrans.readthedocs.io/en/latest/index.html

- petitRADTRANS: https://gitlab.com/mauricemolli/petitRADTRANS
- FastChem: https://github.com/NewStrangeWorlds/FastChem

También se han consultado para realizar los códigos páginas como https://stackoverflow.com/ y herramientas de IA para consultas puntuales (OpenAI, 2023) siendo el autor respponsable de todas la implementaciones finales.
====================
