#%% Imports -------------------------------------------------------------------

import re
import platform
import subprocess
from pathlib import Path

#%% Initialize ----------------------------------------------------------------

ROOT_PATH = Path(__file__).resolve().parents[0]
REPO_NAME = ROOT_PATH.name
ENV_NAME = REPO_NAME.split("_", 1)[1] if "_" in REPO_NAME else REPO_NAME

print(REPO_NAME)
print(ENV_NAME)