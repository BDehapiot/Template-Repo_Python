![Python Badge](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))  
![Author Badge](https://img.shields.io/badge/Author-Benoit_Dehapiot-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))
![Date Badge](https://img.shields.io/badge/Created-2023--09--20-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))
![License Badge](https://img.shields.io/badge/Licence-GNU%20General%20Public%20License%20v3.0-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))    

# Template-Repo_Python-Lite
Template repository for simple Python-based projects
## Description

## Installation
In this tutorial, we will see how to install **Python** using a **Conda** package manager to execute our scripts in a controlled environment with all essential dependencies.  

### 1. Download GitHub repository:  

- Download this repository by clicking the following 
[link](https://github.com/BDehapiot/Template-Repo_Python-Lite/archive/refs/heads/main.zip)  
- Unzip the downloaded folder to a known location (e.g. `Desktop`)

### 2. Install Conda and create a new environment:

We will now install Conda using the light-weight **Miniforge** installer and create a new environment using the `environment.yml` file shipped with this repository.

Select your operating system:  

<details> <summary>Windows</summary>  

- Download Miniforge installer for Windows
([link](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe))  

- Run the downloaded `.exe` file and select the following options:    
    - *create start menu shortcuts*  
    - *add Miniforge3 to PATH environment variable* 

- Run Miniforge Prompt from your start menu shortcuts  

    Your prompt should read something like:  
    `(base) C:\Users\YourUsername>`  
    `(base)` meaning that you are in your base Conda environment 

- Move to your downloaded GitHub repository using the `cd` command: 
    ```bash
    cd Desktop/Template-Repo_Python-Lite-main
    ```
    Your prompt should change to reflect your current location:  
    `(base) C:\Users\YourUsername\Desktop\Template-Repo_Python-Lite-main>`

- Create a new Conda environment (takes a few minutes): 
    ```bash
    mamba env create -f environment.yml
    ```

- Activate the new environment:
    ```bash
    conda activate Python-Lite
    ```
    Your prompt should now display `(Python-Lite)` indicating that you have changed environment   
    `(Python-Lite) C:\Users\YourUsername\Desktop\Template-Repo_Python-Lite-main>`

</details> 

<details> <summary>MacOS</summary>  

- Download Miniforge installer for MacOS 
([legacy](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh))
([M-Series](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh)) 

- Open your terminal by typing `terminal` in the Launchpad  

    Your prompt should read something like:  
    `YourUsername@MacBook-Pro ~ %`

- Move to where you downloaded the Miniforge installer using the `cd` command:  
It is most likely located in your `Downloads` folder    
    ```bash
    cd ~/Downloads
    ```  
    
- Run the following command to install Miniforge:  

    ```bash
    # legacy
    bash Miniforge3-MacOSX-x86_64.sh
    # M-Series
    bash Miniforge3-MacOSX-arm64.sh
    ```  
    Follow the Terminal prompts to complete installation and accept default options  

- Close and re-open your terminal  

    Your prompt should now read something like:  
    `(base) YourUsername@MacBook-Pro ~ %`  
    `(base)` meaning that you are in your base Conda environment  

- Move to your downloaded GitHub repository: 
    ```bash
    cd Desktop/Template-Repo_Python-Lite-main
    ```
    Your prompt should change to reflect your current location:  
    `(base) YourUsername@MacBook-Pro Desktop/Template-Repo_Python-Lite-main %`  

- Create a new Conda environment (takes a few minutes):  
    ```bash
    mamba env create -f environment.yml
    ```

- Activate the new environment:
    ```bash
    conda activate Python-Lite
    ```

    Your prompt should now display `(Python-Lite)` indicating that you have changed environment  
    `(Python-Lite) YourUsername@MacBook-Pro Desktop/Template-Repo_Python-Lite-main %`

</details> 

### 3. Execute Python scripts with Spyder IDE: 

**Spyder** is an Integrated Development Environment (IDE), enabling users to easely execute and interact with Python scripts. Although not mandatory, Spyder is highly recommended for beginners.  

- Activate your new environment and start Spyder using the following command:  
    ```bash
    spyder
    ```

- Create a new project from the Spyder interface:
    - Click `Projects` > `New Project...`
    - Choose `Existing directory`
    - Select the downloaded GitHub repository using the folder icon
    - Click the `Create` button  

    Note: projects can be re-opened later with: `Projects` > `Recent Projects...`

    You can now browse the repository in Spyder and open `.py` files to run Python scripts   

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
