### Step 1: Download this GitHub Repository 
- Click on the green `<> Code` button and download `ZIP` 
- Unzip the downloaded file to a desired location

### Step 2: Install Miniforge (Minimal Conda installer)
- Download and install [Miniforge](https://github.com/conda-forge/miniforge) for your operating system   

#### Windows
- Run the downloaded `.exe` file  
⚠️ Select "Add Miniforge3 to PATH environment variable" 

#### MacOS
- Open your terminal
- Move to the directory containing the Miniforge installer
- Run the following command:  

```bash
# Intel-Series
bash Miniforge3-MacOSX-x86_64.sh
```  
```bash
# M-Series
bash Miniforge3-MacOSX-arm64.sh
```  

### Step 3: Setup Conda 
**Windows** Open the newly installed Miniforge Prompt  
**MacOS** Re-open your terminal 
- Move to the downloaded GitHub repository
- Run the following command: 

```bash
mamba env create -n {{ env_name }} -f environment.yml
```  

```bash
# TensorFlow with GPU support
mamba env create -n {{ env_name }} -f environment-tf-gpu.yml
```  
```bash
# TensorFlow with no GPU support 
mamba env create -n {{ env_name }} -f environment-tf-nogpu.yml
```  

- Activate Conda environment:  
```bash
conda activate {{ env_name }}
```