import numpy as np
import mdshare

mdshare.fetch("alanine-dipeptide-3x250ns-heavy-atom-positions.npz", working_directory="data"
)
mdshare.fetch(
    "alanine-dipeptide-3x250ns-backbone-dihedrals.npz", working_directory="data"
)