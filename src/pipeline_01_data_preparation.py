import os
import argparse
import yaml
import logging

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    #config will have  our default data paths
    #all things which are required and parameters we will use
    #default will be used if config is not passed if we direclty run this file and no config done then default will be used 
    default_config_path = os.path.join("config" ,"params.yaml")
    args.add_argument("--config", default=default_config_path)
    #if we are choosing different datasource we can pass it
    #we can put None as default it will use from config, or we can pass from config
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    print(parsed_args.config, parsed_args.datasource)
    main(config_path = parsed_args.config , datasource = parsed_args.datasource )