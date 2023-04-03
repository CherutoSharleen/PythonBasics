def config_file():
    # path = 'config_file.py'
    # loaded_config = open(path, 'r')
    # return loaded_config
    loaded_config = """# Rocket Ship Configuration File!
        fuel_tanks=4
        oxygen_tanks=3
        initial_propulsion_level=84
        $ End of file"""        
    


    parsed_config = {}
    #split the string to seperate 
    lines = loaded_config.split('\n')
    for line in lines:
        try:
            key, value = line.split('=')
            parsed_config[key] = value
        except ValueError:
            print(f"Unable to parse{line}")
    
    #remove white spaces: leading and trailing
    # for key, value in parsed_config.items():
    #     new_key = key.strip()
    #     parsed_config[new_key] = value
    print(parsed_config)




config_file()