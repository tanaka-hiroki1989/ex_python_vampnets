import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import mdshare  
from tqdm.notebook import tqdm

if torch.cuda.is_available():
    device = torch.device("cuda")
    torch.backends.cudnn.benchmark = True
else:
    device = torch.device("cpu")
torch.set_num_threads(12)

print(f"Using device {device}")