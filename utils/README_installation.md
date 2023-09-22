<details> <summary>Windows</summary>

### 1 - Download GitHub repository: 
- Download GitHub repository
([link](https://github.com/BDehapiot/ETH-ScopeM_CZITools/archive/refs/heads/main.zip)) 
- Unzip folder to a known location (e.g. `C:\Users\YourUsername\Desktop`)

### 2 - Install Mambaforge: 
- Download Mambaforge installer for Windows 
([link](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe))
- Run the downloaded `.exe` file and select the following options:  
    - create start menu shortcuts
    - add Miniforge3 to PATH environment variable

### 3 - Setup mamba/conda environment: 
- Run `Miniforge Prompt` from start menu shortcuts (see `Miniforge3` folder)
- Your prompt should look like this:  
```bash
(base) PS C:\Users\YourUsername>
```
    - ⚠️`(base)` indicates that you are in your base environment




- Move the prompt to the downloaded GitHub repository using the `cd` command: 
```bash
cd Desktop/{{ repo_name }}-main
```
- The prompt should change to reflect your current location:
```bash
(base) PS C:\Users\YourUsername>\Desktop\{{ repo_name }}-main
```
- You can now create a new mamba/conda environment: 
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

⚠️ `(base)` at the beginning of the prompt means that you are in your base mamba/conda environment