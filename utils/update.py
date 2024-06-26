#%% Imports -------------------------------------------------------------------

import yaml
import urllib
import requests
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

# Paths
root_path = Path(__file__).resolve().parents[1]
utils_path = root_path / "utils"
repo_name = root_path.name

# Read config.yml
with open(Path(root_path / "utils" / "config.yml"), 'r') as file:
    config = yaml.safe_load(file)    
env_name = config.get('env_name', [])[0]
env_type = config.get('env_type', [])[0]
install = config.get('install', [])[0]

# Manage environment files
if env_type == "base":
    for path in list(root_path.glob("*environment*")):
        if path.stem != "environment":
            path.rename(utils_path / path.name)
if env_type == "tf-gpu":
    for path in list(root_path.glob("*environment*")):
        if path.stem == "environment":
            path.rename(utils_path / path.name)
    for path in list(utils_path.glob("*environment*")):
        if "-tf-" in path.stem :
            path.rename(root_path / path.name)
            
#%% Read files ----------------------------------------------------------------

# Read environment.yml
if env_type == "base":
    with open(Path(root_path / "environment.yml"), 'r') as file:
        environment = yaml.safe_load(file)
if env_type == "tf-gpu":
    with open(Path(root_path / "environment-tf-gpu.yml"), 'r') as file:
        environment = yaml.safe_load(file)

# Read README_template.md
with open(Path(utils_path / "README_template.md"), "r") as file:
    template = file.read()

# Read README_main.md
with open(Path(utils_path / "README_main.md"), "r") as file:
    main = file.read()

# Read README_installation.md
if install == "full":
    with open(Path(utils_path / "README_installation-full.md"), "r") as file:
        installation = file.read()
if install == "lite":
    with open(Path(utils_path / "README_installation-lite.md"), "r") as file:
        installation = file.read()

#%% Extract relevant informations ---------------------------------------------

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

# Extract conda and pip dependencies
conda_dependencies = []
pip_dependencies = []
for dependency in environment.get('dependencies', []):
    if isinstance(dependency, str):
        conda_dependencies.append(dependency)
        if dependency.startswith('python='):
            python_version = dependency.split('=')[1]
        # if env_type == "tf-gpu":
        #     if dependency.startswith('cudatoolkit='):
        #         cuda_version = dependency.split('=')[1]
        #     if dependency.startswith('cudnn='):
        #         cudnn_version = dependency.split('=')[1]
    elif isinstance(dependency, dict) and 'pip' in dependency:
        pip_dependencies.extend(dependency['pip'])
        # if env_type == "tf-gpu":
        #     if dependency.startswith('tensorflow'):
        #         cuda_version = dependency.split('=')[1]

#%% Format and replace --------------------------------------------------------

# Format conda and pip dependencies
conda_dependencies_str = ""
for dependency in conda_dependencies:
    conda_dependencies_str += f"- {dependency}\n"
pip_dependencies_str = ""
for dependency in pip_dependencies:
    pip_dependencies_str += f"- {dependency}\n"

# Replace placeholders
installation = installation.replace("{{ repo_name }}", repo_name)
installation = installation.replace("{{ env_name }}", env_name)
template = template.replace("{{ repo_name }}", repo_name)
template = template.replace("{{ python_version }}", python_version)
template = template.replace("{{ license }}", license)
template = template.replace("{{ date }}", date)
template = template.replace("{{ short_description }}", short_description)
template = template.replace("{{ main }}", main)
template = template.replace("{{ installation }}", installation)
# template = template.replace("{{ conda_dependencies }}", conda_dependencies_str)
# template = template.replace("{{ pip_dependencies }}", pip_dependencies_str)

#%% Update README -------------------------------------------------------------

# # Write README.md in root path
# with open(Path(root_path / "README.md"), "w") as file:
#     file.write(template)