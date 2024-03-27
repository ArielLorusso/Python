# FIND NVIDIA CUDA LINUX
https://www.cyberciti.biz/faq/how-to-find-the-nvidia-cuda-version/

# PIP Nvidia
```sh
ariel $ pip list | grep nvidia
nvidia-cublas-cu11       11.10.3.66
nvidia-cuda-cupti-cu11   11.7.101
nvidia-cuda-nvrtc-cu11   11.7.99
nvidia-cuda-runtime-cu11 11.7.99
nvidia-cudnn-cu11        8.5.0.96
nvidia-cufft-cu11        10.9.0.58
nvidia-curand-cu11       10.2.10.91
nvidia-cusolver-cu11     11.4.0.1
nvidia-cusparse-cu11     11.7.4.91
nvidia-nccl-cu11         2.14.3
nvidia-nvtx-cu11         11.7.91
```
# PIP PyTorch
```sh
ariel $ pip list | grep torch
torch                    2.0.0
torchaudio               2.0.1
torchvision              0.15.1
```
# PIP Detectron 2
    https://detectron2.readthedocs.io/en/latest/tutorials/install.html
```sh
# detectron2  INSTALLATION 
 python3 -m pip install detectron2 -f   https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html 
 python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
```
```sh
ariel  $ pip list | grep detect
detectron2               0.6
```

# OS INFO
```sh
ariel  $  cat /etc/os-release
PRETTY_NAME="Linux Mint 21.2"
VERSION=    "21.2 (Victoria)"
ID_LIKE=    "ubuntu debian"
VERSION_CODENAME=   victoria  # MINT   21.2
UBUNTU_CODENAME=    jammy     # UBUNTU 22.04
```



# CHECK CUDA in PyTorch
```py
# cudaRuntimeGetVersion()
import torch
# TEST CUDA device               
torch.cuda.set_device(0)            # Use 0 or the GPU device index you want to use
torch.cuda.is_available()           # Aviable ? 
```

# CHECK GPU AVIABLES        sudo apt install nvidia-utils-470     
```sh
Sun Nov 26 23:52:48 2023                                     CUDA Version: 12.3
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 545.23.08              Driver Version: 545.23.08    CUDA Version: 12.3     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce GTX 1050 Ti     On  | 00000000:01:00.0  On |                  N/A |
| 35%   36C    P0              N/A /  75W |    566MiB /  4096MiB |      2%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+  
```

```sh
nvcc --version                             # sudo apt install nvidia-cuda-toolkit
# did not test this  ( NOT necesary)     https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html
```  

# CUDA COMPATIBILITY
    https://docs.nvidia.com/deploy/cuda-compatibility/

# INSTALL Nvidia's   cuda-toolkit
    https://developer.nvidia.com/cuda-toolkit

### METHOD 1   ( apt-get install )          WORKED  OK  !
`https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_network`
``` sh
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
    sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
    sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
    sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
    sudo apt-get update
    sudo apt-get -y install cuda 
```
### METHOD 2    INSTALL SPECIFIC VERSION    FAIL ! 
        Chat-GPT suggestion 
```sh
    wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_465.19.01_linux.run
    sudo sh cuda_11.7.0_465.19.01_linux.run
```
` `  
    For CUDA 11.4 (replace the URL with the appropriate version)
    FAIL --> verify gcc version :
``` sh
    wget https://developer.download.nvidia.com/compute/cuda/11.4.0/local_installers/cuda_11.4.0_470.42.01_linux.run
    sudo sh cuda_11.4.0_470.42.01_linux.run   """
```

# CHECK  nvidia-cuda-toolkit  VERSION
```sh
apt version nvidia-cuda-toolkit
#   11.5.1-1ubuntu1
```

# Stack Overflow  CUDA  &detectron2 
```py   
#  https://stackoverflow.com/questions/70910160/detectron2-cuda-is-not-available
#  https://stackoverflow.com/questions/9727688/how-to-get-the-cuda-version
```



# https://www.ccoderun.ca/programming/doxygen/opencv/group__imgproc.html
# https://www.ccoderun.ca/programming/doxygen/opencv/group__features2d.html