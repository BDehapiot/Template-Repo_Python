conda_create_base[
```bash
mamba env create -n {{ env_name }} -f environment.yml
```  
]

conda_create_tensorflow[
```bash
# TensorFlow with GPU support
mamba env create -n {{ env_name }} -f environment-tf-gpu.yml
```  
```bash
# TensorFlow with no GPU support 
mamba env create -n {{ env_name }} -f environment-tf-nogpu.yml
```
]