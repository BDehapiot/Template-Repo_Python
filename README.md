![Python Badge](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))  
![Author Badge](https://img.shields.io/badge/Author-Benoit_Dehapiot-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))  
![License Badge](https://img.shields.io/badge/Licence-GNU_General_Public_License_v3.0-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))  


# Template-Repo_Python-Lite
## Description

## Installation
This tutorial provides a step-by-step guide to install Python, coupled with Spyder, using the Conda/Mamba environment manager.  

The **Conda/Mamba** environment manager allows to run Python code within a controlled environment that contains all necessary dependencies. It's a best practice to create a distinct environment for each Python-based projects. 

**Spyder** is an Integrated Development Environment (IDE), enabling users to easely execute and interact with Python codes. Although not mandatory, Spyder is highly recommended for beginners.  

Select your operating system:

<details> <summary>Windows</summary>  

### Download GitHub repository:  

1) Download this GitHub repository
([link](https://github.com/BDehapiot/ETH-ScopeM_CZITools/archive/refs/heads/main.zip)) 

2) Unzip folder to a known location (e.g. `C:\Users\YourUsername\Desktop`)

### Install Mambaforge:  

3) Download Mambaforge installer for Windows
([link](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe))  

4) Run the downloaded `.exe` file and select the following options:    
    - *create start menu shortcuts*  
    - *add Miniforge3 to PATH environment variable*  

### Setup Conda/Mamba environment: 

5) Run **Miniforge Prompt** from start menu shortcuts  

    The prompt should read:  
    `(base) C:\Users\YourUsername>`  
    `(base)` meaning that we are in our base environment  

6) Move to the downloaded GitHub repository using the `cd` command: 
    ```bash
    cd Desktop/Template-Repo_Python-Lite-main
    ```
    The prompt should change to reflect your current location:  
    `(base) C:\Users\YourUsername\Desktop\Template-Repo_Python-Lite-main>`

7) Create a new Mamba/Conda environment (takes a few minutes): 
    ```bash
    mamba env create -f environment.yml
    ```

8) Activate the newly created environment:
    ```bash
    conda activate Python-Lite
    ```
    The prompt should now start with `(Python-Lite)`  
    `(Python-Lite) C:\Users\YourUsername\Desktop\Template-Repo_Python-Lite-main>`

### Start and setup Spyder IDE: 

9) Start Spyder using the following command:
    ```bash
    spyder
    ```

10) Create a new Spyder project
    - Click the `Projects` > `New Project...`
    - Choose `Existing directory`
    - Select the GitHub repository using the folder icon
    - Click the `Create` button  

    Projects can be re-opened later with: `Projects` > `Recent Projects...`

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
