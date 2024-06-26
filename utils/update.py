#%% Imports -------------------------------------------------------------------

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

def format_dependencies(dependencies, indent=2):
    dependencies = [f"\n{' ' * indent}- " + dep for dep in dependencies]
    dependencies = "".join(dependencies)
    return dependencies

def update_environment(path):    
       
    # Read YML environment file
    with open(path, "r") as file:
        environment = file.read()
        
    # Replace placeholders
    environment = environment.replace("{{ env_name }}", env_name)
    environment = environment.replace("{{ python_version }}", python_version)
    environment = environment.replace("{{ dep_conda }}", dep_conda)
    environment = environment.replace("{{ dep_pip }}", dep_pip)
    
    # Save YML environment file
    with open(root_path / path.name, "w") as file:
        file.write(environment)
  
def update_readme():
    
    # Read MD Readme files
    with open(Path(utils_path / f"README_install-{rdm_install}.md"), "r") as file:
        install = file.read()
    with open(Path(utils_path / "README_main.md"), "r") as file:
        main = file.read()
    with open(Path(utils_path / "README_template.md"), "r") as file:
        template = file.read()
        
    # Replace placeholders
    install = install.replace("{{ repo_name }}", repo_name)
    install = install.replace("{{ env_name }}", env_name)
    template = template.replace("{{ repo_name }}", repo_name)
    template = template.replace("{{ python_version }}", python_version)
    template = template.replace("{{ license }}", license)
    template = template.replace("{{ date }}", date)
    template = template.replace("{{ short_description }}", short_description)
    template = template.replace("{{ main }}", main)
    template = template.replace("{{ install }}", install)
    
    # Save MD Readme file
    with open(Path(root_path / "README.md"), "w") as file:
        file.write(template)  

#%% Initialize ----------------------------------------------------------------

# Parse INI config file
config = ConfigParser()
config.read(utils_path / 'config.ini')
env_name = config['environment']['name']
env_type = config['environment']['type']
python_version = config['python']['version']
dep_conda = config['dependencies']['conda'].split(', ')
dep_pip = config['dependencies']['pip'].split(', ')
rdm_install = config['readme']['install']

# Format dependencies
if dep_conda[0] != "None": 
    dep_conda = format_dependencies(dep_conda, indent=2)
else: dep_conda = ""
if dep_pip[0] != "None": 
    dep_pip = format_dependencies(dep_pip, indent=4)
else: dep_pip = ""

# Extract repository data
repo_data = requests.get(
    f"https://api.github.com/repos/BDehapiot/{repo_name}", 
    headers={}
    ).json()
date = repo_data["created_at"][:10]
date = date.replace("-", "--")
date = urllib.parse.quote(date)
license = urllib.parse.quote(repo_data["license"]["name"])
short_description = repo_data["description"]

#%% Execute -------------------------------------------------------------------

# Remove preexisting files
for path in list(root_path.glob("*environment*")):
    path.unlink()
for path in list(root_path.glob("*readme*")):
    path.unlink()

# Update files
if env_type == "base":
    update_environment(utils_path / "environment.yml")
if env_type == "tf-gpu":
    update_environment(utils_path / "environment-tf-gpu.yml")
    update_environment(utils_path / "environment-tf-nogpu.yml")
update_readme()