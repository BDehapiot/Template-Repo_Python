<details> <summary>Windows</summary>

### 1 - Download GitHub repository: 
- Download GitHub repository
([link](https://github.com/BDehapiot/ETH-ScopeM_CZITools/archive/refs/heads/main.zip)) 
- Unzip the file to a known location (e.g. `C:\Users\YourUsername\Desktop`)

### 2 - Install Mambaforge: 
- Download Mambaforge installer for Windows 
([link](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe))
- Run the downloaded `.exe` file and select the following options:
    - 🗸 create start menu shortcuts
    - 🗸 add Miniforge3 to PATH environment variable

### 3 - Setup mamba/conda environment: 
- Start `Miniforge Prompt` from the newly installed Miniforge3 folder (see `Start Menu`)
- Your prompt should look like this: 
 ```bash
(base) PS C:\Users\YourUsername>
```
⚠️ `(base)` at the beginning of the prompt means that you are in your base mamba/conda environment
- Navigate to the downloaded GitHub repository using the `cd` command: 
 ```bash
cd Desktop/{{ repo_name }}-main
```
- The prompt should change to reflect your current location:
 ```bash
(base) PS C:\Users\YourUsername>\Desktop\{{ repo_name }}-main
```
- Create a new environment: 
 ```bash
mamba env create -f environment.yml
```
- Activate your newly created environment:
 ```bash
mamba activate {{ env_name }}
```
- Your prompt should now start with `({{ env_name }})`

<hr style=\"border-top: 1px\">
</details>