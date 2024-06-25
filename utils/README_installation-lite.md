### Step 1: Download GitHub Repository 
- Click on the green `<> Code` button and download `ZIP` 
- Unzip the downloaded file to a desired location

### Step 2: Install Miniforge
- Download **Miniforge installer** for your operating system:  
https://github.com/conda-forge/miniforge  

#### Windows
- Run the downloaded `.exe` file 
- Select "Add Miniforge3 to PATH environment variable" 

#### MacOS
- Open your terminal
- Move to the directory containing the **Miniforge installer**
- Run the following command:  

```bash
# Intel-Series
bash Miniforge3-MacOSX-x86_64.sh
# M-Series
bash Miniforge3-MacOSX-arm64.sh
```  

### Step 3: Setup Conda Environment
- Open the newly installed **Miniforge Prompt**
- Move to the downloaded GitHub repository
- Run the following command: 

```bash
mamba env create -n {{ env_name }} -f environment.yml
```  

```bash
# GPU support (NVIDIA)
mamba env create -n {{ env_name }} -f environment-gpu.yml
# no GPU support 
mamba env create -n {{ env_name }} -f environment-nogpu.yml
```  

- Activate Conda environment:  
```bash
conda activate {{ env_name }}
```