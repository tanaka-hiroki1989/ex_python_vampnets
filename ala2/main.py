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

with np.load("data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz") as fh:
    data = [fh[f"arr_{i}"].astype(np.float32) for i in range(3)]
with np.load("data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz") as fh:
    dihedral = [fh[f"arr_{i}"] for i in range(3)]

def plot_dihedral(dihedral,image_path):
    f, ax = plt.subplots(1, 1)
    hb = ax.hexbin(*np.concatenate(dihedral).T, mincnt=5)
    ax.set_aspect('equal')
    cb = f.colorbar(hb, ax=ax)
    cb.set_label('# of frames in bin')
    plt.savefig(image_path)

plot_dihedral(dihedral,"fig/dihedral_plane.png")