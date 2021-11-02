import os
import argparse
import yaml
import logging


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    #config will have  our default data paths
    #all things which are required and parameters we will use
    #default will be used if config is not passed if we direclty run this file and no config done then default will be used 
    args.add_argument("--config", default="default")
    #if we are choosing different datasource we can pass it
    #we can put None as default it will use from config, or we can pass from config
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    print(parsed_args.config, parsed_args.datasource)