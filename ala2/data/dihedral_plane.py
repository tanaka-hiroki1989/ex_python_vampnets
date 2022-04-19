import matplotlib.pyplot as plt
import numpy as np
from plot import plot_dihedral

with np.load("data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz") as fh:
    dihedral = [fh[f"arr_{i}"] for i in range(3)]

plot_dihedral(dihedral,"fig/dihedral_plane.png")