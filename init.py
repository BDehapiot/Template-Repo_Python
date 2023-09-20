#%% Imports -------------------------------------------------------------------

import re
import platform
import subprocess
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path(__file__).resolve().parents[0]
REPO_NAME = ROOT_PATH.name
ENV_NAME = REPO_NAME.split("_", 1)[1] if "_" in REPO_NAME else REPO_NAME

#%% Replace placeholders ------------------------------------------------------

def replace_placeholders(file_path):
    
    # Read file
    with open(file_path, "r") as file:
        txt = file.read()

    # Replace placeholders
    txt = txt.replace("{{ env_name }}", ENV_NAME)
    txt = txt.replace("{{ env_name }}", ENV_NAME)

    # Update file
    with open(file_path, "w") as file:
        file.write(txt)

replace_placeholders(Path(ROOT_PATH / "environment.yml"))
