from config import np, os

def export_data(modo, dir_main, mass_fractions, wavelengths_cm, radio_transito_cm, params_basic, depth_ppm):
    """
    Exporta los datos obtenidos en el main.py para después utilizarlos para hacer gráficas, etc. con un script diferente especializado en hacer gráficas (plot_master.py)

    Args: modo, dir_main, mass_fractions, wavelengths_cm, radio_transito_cm, params_basic, depth_ppm

    Return: archivos txt guardado en la carpeta correspondiente a cada caso en la carpeta output data
    """    
    if params_basic.case_label == 'ben1':

        file_path_1 = os.path.join(dir_main, "output_data", "ben1", f"output_data_{params_basic.case_label}_{modo}_atm.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "ben1", f"output_data_{params_basic.case_label}_{modo}_spectrum.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")
        
    elif params_basic.case_label == 'ben2':

        file_path_1 = os.path.join(dir_main, "output_data", "ben2", f"output_data_{params_basic.case_label}_{modo}_atm.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "ben2", f"output_data_{params_basic.case_label}_{modo}_spectrum.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")

    elif params_basic.case_label == 'hab1':

        file_path_1 = os.path.join(dir_main, "output_data", "hab1", f"output_data_{params_basic.case_label}_{modo}_atm_micras.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "hab1", f"output_data_{params_basic.case_label}_{modo}_spectrum_micras.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")

    elif params_basic.case_label == 'ben1_noCO2':

        file_path_1 = os.path.join(dir_main, "output_data", "ben1", f"output_data_{params_basic.case_label}_{modo}_atm.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "ben1", f"output_data_{params_basic.case_label}_{modo}_spectrum.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")

    elif params_basic.case_label == 'ben1_noCIA':

        file_path_1 = os.path.join(dir_main, "output_data", "ben1", f"output_data_ben1_noCIA_{modo}_atm.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "ben1", f"output_data_ben1_noCIA_{modo}_spectrum.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")

    elif params_basic.case_label == 'ben2_noCIA':

        file_path_1 = os.path.join(dir_main, "output_data", "ben2", f"output_data_ben2_noCIA_{modo}_atm.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "ben2", f"output_data_ben2_noCIA_{modo}_spectrum.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")

    elif params_basic.case_label == 'hab1':

        file_path_1 = os.path.join(dir_main, "output_data", "hab1", f"output_data_{params_basic.case_label}_{modo}_atm.txt")
        file_path_2 = os.path.join(dir_main, "output_data", "hab1", f"output_data_{params_basic.case_label}_{modo}_spectrum.txt")
                
        values_mass_fraction = np.column_stack(list(mass_fractions.values()))
        header_mass_fractions = " ".join([f"Mass_fraction_{key}" for key in mass_fractions.keys()])

        np.savetxt(file_path_1, np.column_stack((params_basic.temperatures_K, params_basic.pressures_bar, params_basic.z_km, values_mass_fraction)), header=f"Temperatures_K Pressures_bar z_km {header_mass_fractions}")
        np.savetxt(file_path_2, np.column_stack((wavelengths_cm, radio_transito_cm, depth_ppm)), header=f"wavelengths_cm Transit_radius_cm depth_ppm")
        
        
