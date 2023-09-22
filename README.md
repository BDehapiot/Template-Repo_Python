![Author Badge](https://img.shields.io/badge/Author-Benoit_Dehapiot-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))  
![License Badge](https://img.shields.io/badge/Licence-GNU_General_Public_License_v3.0-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))  
![Python Badge](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))

# Template-Repo_Python-Lite
## Description
{{ description }}
## Installation
<details> <summary>Windows</summary>  
<br>This is a step by step guide to 

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

### Setup Mamba/Conda environment: 

5) Run `Miniforge Prompt` from start menu shortcuts (see `Miniforge3` folder)  
<br>The prompt should look like this:  
    ```bash
    (base) PS C:\Users\YourUsername>
    ```
    `(base)` at the beginning of the prompt means that you are in your base environment

6) Move to the downloaded GitHub repository using the `cd` command: 
    ```bash
    cd Desktop/Template-Repo_Python-Lite-main
    ```
    The prompt should change to reflect your current location:
    ```bash
    (base) PS C:\Users\YourUsername\Desktop\Template-Repo_Python-Lite-main>
    ```

7) Create a new Mamba/Conda environment: 
    ```bash
    mamba env create -f environment.yml
    ```

8) Activate the newly created environment:
    ```bash
    mamba activate Python-Lite
    ```

    The prompt should now start with `(Python-Lite)`
    ```bash
    (Python-Lite) PS C:\Users\YourUsername\Desktop\Template-Repo_Python-Lite-main>
    ```

### Setup Spyder IDE: 

<hr style=\"border-top: 1px\">
</details>  

## Dependencies
### Conda
- python=3.10
- numpy
- scipy
- scikit-image
- pandas
- opencv
- joblib
- matplotlib-base
- pyyaml
- pip

### pip
- napari[all]
- spyder
