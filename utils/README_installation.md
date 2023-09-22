<details> <summary>Windows</summary>  
<br>This is a step by step guide to install Python using the Mamba/Conda
environment manager.  

While all steps are required to complete installation, only steps 5, 6, 8, 9 will be later necessary to 

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
    (base) C:\Users\YourUsername>
    ```
    `(base)` at the beginning of the prompt means that you are in your base environment

6) Move to the downloaded GitHub repository using the `cd` command: 
    ```bash
    cd Desktop/{{ repo_name }}-main
    ```
    The prompt should change to reflect your current location:
    ```bash
    (base) C:\Users\YourUsername\Desktop\{{ repo_name }}-main>
    ```

7) Create a new Mamba/Conda environment (takes a few minutes): 
    ```bash
    mamba env create -f environment.yml
    ```

8) Activate the newly created environment:
    ```bash
    mamba activate {{ env_name }}
    ```

    The prompt should now start with `({{ env_name }})`
    ```bash
    ({{ env_name }}) C:\Users\YourUsername\Desktop\{{ repo_name }}-main>
    ```

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

    Note: Re-open your project using `Projects` > `Recent Projects...`
</details>  
