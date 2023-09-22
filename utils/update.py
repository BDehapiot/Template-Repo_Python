#%% Imports -------------------------------------------------------------------

import yaml
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

root_path = Path(__file__).resolve().parents[1]
repo_name = root_path.name

#%% Extract relevant info -----------------------------------------------------

# Read environment.yml
with open(Path(root_path / "environment.yml"), 'r') as file:
    yml = yaml.safe_load(file)

# Extract environment name
env_name = yml.get('name', '')

# Extract conda and pip dependencies
conda_dependencies = []
pip_dependencies = []
for dependency in yml.get('dependencies', []):
    if isinstance(dependency, str):
        conda_dependencies.append(dependency)
        if dependency.startswith('python='):
            python_version = dependency.split('=')[1]
    elif isinstance(dependency, dict) and 'pip' in dependency:
        pip_dependencies.extend(dependency['pip'])

# Format conda and pip dependencies
conda_dependencies_str = ""
for dependency in conda_dependencies:
    conda_dependencies_str += f"- {dependency}\n"
pip_dependencies_str = ""
for dependency in pip_dependencies:
    pip_dependencies_str += f"- {dependency}\n"
print(pip_dependencies_str)

# Extract installation instructions
with open(Path(root_path / "utils" / "README_description.md"), "r") as file:
    description = file.read()

# Extract installation instructions
with open(Path(root_path / "utils" / "README_installation.md"), "r") as file:
    installation = file.read()

# Replace placeholders
installation = installation.replace("{{ repo_name }}", repo_name)
installation = installation.replace("{{ env_name }}", env_name)

#%% Update README -------------------------------------------------------------

# Read README_template.md
with open(Path(root_path / "utils" / "README_template.md"), "r") as file:
    txt = file.read()

# Replace placeholders
txt = txt.replace("{{ repo_name }}", repo_name)
txt = txt.replace("{{ env_name }}", env_name)
txt = txt.replace("{{ python_version }}", python_version)
txt = txt.replace("{{ description }}", description)
txt = txt.replace("{{ installation }}", installation)
txt = txt.replace("{{ conda_dependencies }}", conda_dependencies_str)
txt = txt.replace("{{ pip_dependencies }}", pip_dependencies_str)

# Write README.md in root path
with open(Path(root_path / "README.md"), "w") as file:
    file.write(txt)