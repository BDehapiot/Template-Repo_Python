<details> <summary>Windows</summary>

### Download GitHub repository: 
1) Download GitHub repository
([link](https://github.com/BDehapiot/ETH-ScopeM_CZITools/archive/refs/heads/main.zip)) 
2) Unzip folder to a known location (e.g. `C:\Users\YourUsername\Desktop`)

### Install Mambaforge: 
3) Download Mambaforge installer for Windows 
([link](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe))
4) Run the downloaded `.exe` file and select the following options:  
    - create start menu shortcuts
    - add Miniforge3 to PATH environment variable

### 3 - Setup mamba/conda environment: 

5) Run `Miniforge Prompt` from start menu shortcuts (see `Miniforge3` folder)  
<br>
The prompt should look like this:  
    ```bash
    (base) PS C:\Users\YourUsername>
    ```
    `(base)` at the beginning of the prompt means that you are in your base environment
<br><br>

6) Move to the downloaded GitHub repository using the `cd` command: 
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

- Activate the newly created environment:
```bash
mamba activate {{ env_name }}
```

- The prompt should now start with `({{ env_name }})`
```bash
mamba activate {{ env_name }}
```

### 4 - Start Spyder IDE and create a project: 

<hr style=\"border-top: 1px\">
</details>