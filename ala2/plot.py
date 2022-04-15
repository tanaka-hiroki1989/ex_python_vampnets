import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from tqdm.notebook import tqdm

def plot_dihedral(dihedral,image_path):
    f, ax = plt.subplots(1, 1)
    hb = ax.hexbin(*np.concatenate(dihedral).T, mincnt=5)
    ax.set_aspect('equal')
    cb = f.colorbar(hb, ax=ax)
    cb.set_label('# of frames in bin')
    plt.savefig(image_path)

