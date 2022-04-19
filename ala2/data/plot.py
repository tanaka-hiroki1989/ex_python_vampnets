import matplotlib.pyplot as plt
import numpy as np


def plot_dihedral(dihedral,image_path):
    f, ax = plt.subplots(1, 1)
    hb = ax.hexbin(*np.concatenate(dihedral).T, mincnt=5)
    ax.set_aspect('equal')
    ax.set_xlim(-np.pi,np.pi)
    ax.set_ylim(-np.pi,np.pi)
    ax.set_xticks([-np.pi,0.0,np.pi])
    ax.set_xticklabels(['-π','0','π'])   
    ax.set_yticks([-np.pi,0.0,np.pi])
    ax.set_yticklabels(['-π','0','π'])   
    cb = f.colorbar(hb, ax=ax)
    cb.set_label('# of frames in bin')
    plt.savefig(image_path)

