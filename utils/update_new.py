#%% Imports -------------------------------------------------------------------

import re
import urllib
import requests
from pathlib import Path
from configparser import ConfigParser

#%% Inputs --------------------------------------------------------------------

# Paths
root_path = Path(__file__).resolve().parents[1]
utils_path = root_path / "utils"
repo_name = root_path.name

#%% Functions -----------------------------------------------------------------

def parse_dependencies(item):
    dependency_list = []
    for key, value in config.items(item):
        if key:            
            if "conda" in item:
                ident = " " * 2
                if value: 
                    dependency_list.append(f"\n{ident}- {key}={value}")
                else: 
                    dependency_list.append(f"\n{ident}- {key}")            
            if "pip" in item:
                ident = " " * 4
                if value: 
                    dependency_list.append(f"\n{ident}- {key}={value}")
                else: 
                    dependency_list.append(f"\n{ident}- {key}")
        else:
            dependency_list = ""
    return dependency_list

def update_environment(path):
    with open(path, "r") as file:
        environment = file.read()
    environment = environment.replace("{{ env_name }}", "".join(env_name))
    environment = environment.replace("{{ conda_core }}", "".join(conda_core))
    environment = environment.replace("{{ conda_spec }}", "".join(conda_spec))
    environment = environment.replace("{{ pip_core }}", "".join(pip_core))
    environment = environment.replace("{{ pip_spec }}", "".join(pip_spec))
    if "gpu" in path.name:
        environment = environment.replace("{{ conda_tf_gpu }}", "".join(conda_tf_gpu))
        environment = environment.replace("{{ conda_tf_nogpu }}", "".join(conda_tf_nogpu))
        environment = environment.replace("{{ pip_tf_gpu }}", "".join(pip_tf_gpu))
        environment = environment.replace("{{ pip_tf_nogpu }}", "".join(pip_tf_nogpu))
    return environment

def update_install(path):
    with open(path, "r") as file:
        install = file.read()
    return install

#%% Initialize ----------------------------------------------------------------

# Parse INI config file
config = ConfigParser()
config.read(utils_path / 'config.ini')
env_name = config['environment']['name']
env_type = config['environment']['type']
rdm_install = config['readme']['install']
test = config["install"]["conda_base"]

#%% Execute -------------------------------------------------------------------

# Parse dependencies
conda_core = parse_dependencies("conda_core")
conda_spec = parse_dependencies("conda_spec")
pip_core = parse_dependencies("pip_core")
pip_spec = parse_dependencies("pip_spec")
if env_type == "tensorflow":
    conda_tf_gpu = parse_dependencies("conda_tf_gpu")
    conda_tf_nogpu = parse_dependencies("conda_tf_nogpu")
    pip_tf_gpu = parse_dependencies("pip_tf_gpu")
    pip_tf_nogpu = parse_dependencies("pip_tf_nogpu")
    
# Update YML environment files
if env_type == "base":
    environment = update_environment(utils_path / "environment.yml")
elif env_type == "tensorflow":
    environment_tf_gpu = update_environment(
        utils_path / "environment_tf_gpu.yml")
    environment_tf_nogpu = update_environment(
        utils_path / "environment_tf_nogpu.yml")

# Update MD readme files
if rdm_install == "lite":
    install = update_install(utils_path / "README_install-lite.md")
    

