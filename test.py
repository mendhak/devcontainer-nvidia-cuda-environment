import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("CUDA device name:", torch.cuda.get_device_name(0))
    x = torch.rand(3, 3).cuda()
    print("Tensor on CUDA:", x)
else:
    print("CUDA not available.")
    
    raise RuntimeError("CUDA is not available. This application requires a CUDA-enabled GPU.")

 
from pathlib import Path

def is_docker():
    cgroup = Path('/proc/self/cgroup')
    return Path('/.dockerenv').is_file() or (cgroup.is_file() and 'docker' in cgroup.read_text())

print("Running inside Docker:", is_docker())