![Python Badge](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))  
![TensorFlow Badge](https://img.shields.io/badge/TensorFlow-2.10-green?logo=TensorFlow&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))
![CUDA Badge](https://img.shields.io/badge/CUDA-11.2-green?logo=NVIDIA&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))
![cuDNN Badge](https://img.shields.io/badge/cuDNN-8.1-green?logo=NVIDIA&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))  
![Author Badge](https://img.shields.io/badge/Author-Benoit_Dehapiot-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))
![Date Badge](https://img.shields.io/badge/Created-2023--09--20-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))
![License Badge](https://img.shields.io/badge/Licence-GNU%20General%20Public%20License%20v3.0-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))    

# Template-Repo_Python-Lite
Template repository for simple Python-based projects
## Content

## Outputs
## Installation
### Step 1: Download GitHub Repository 
- Click on the green `<> Code` button and `Download ZIP` 
- Unzip the downloaded file at a desired location

### Step 2: Install Miniforge (Minimal Conda installer)
- Download and install [Miniforge](https://github.com/conda-forge/miniforge) for your operating system  
 
<details> <summary>Windows</summary>  

- Run the downloaded `.exe` file 
- Select "Add Miniforge3 to PATH environment variable" 

</details> 

<details> <summary>MacOS</summary>  

- Open your terminal
- Move to the directory containing the Miniforge installer
- Run the following command:  

```bash
# Intel-Series
bash Miniforge3-MacOSX-x86_64.sh
# M-Series
bash Miniforge3-MacOSX-arm64.sh
```  

</details> 

### Step 3: Setup Conda Environment
- Open a newly installed Miniforge Prompt
- Move to the downloaded GitHub repository
- Run the following command: 

```bash
mamba env create -n Python-Lite -f environment.yml
```  

```bash
# GPU support
mamba env create -n Python-Lite -f environment-tf-gpu.yml
# No GPU support 
mamba env create -n Python-Lite -f environment-tf-nogpu.yml
```  

- Activate Conda environment:  
```bash
conda activate Python-Lite
```