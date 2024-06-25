![Python Badge](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=rgb(149%2C157%2C165)&labelColor=rgb(50%2C60%2C65))  
![Author Badge](https://img.shields.io/badge/Author-Benoit_Dehapiot-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))
![Date Badge](https://img.shields.io/badge/Created-2023--09--20-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))
![License Badge](https://img.shields.io/badge/Licence-GNU%20General%20Public%20License%20v3.0-blue?labelColor=rgb(50%2C60%2C65)&color=rgb(149%2C157%2C165))    

# Template-Repo_Python-Lite
Template repository for simple Python-based projects
## Content

## Outputs
## Installation
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
mamba env create -n Python-Lite -f environment.yml
```  

```bash
# TensorFlow with GPU support
mamba env create -n Python-Lite -f environment-tf-gpu.yml
# TensorFlow with no GPU support 
mamba env create -n Python-Lite -f environment-tf-nogpu.yml
```  

- Activate Conda environment:  
```bash
conda activate Python-Lite
```
## Author
**Benoit Dehapiot** - PhD  
Image Data Analyst  
<span style="color:red;">Image Data Analyst</span>  
***ETH****zürich* - ScopeM  

