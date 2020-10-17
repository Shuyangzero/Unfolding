from unfold import EBS_scatter
from unfold import unfold, make_kpath
import numpy as np
import os

# basis vector of the primitive cell
fermi = os.popen('grep fermi OUTCAR').read().split()[14]
M = [[0.,  1., -1., ], [1., -1.,  0.], [-9., -9., -9.]]
WaveSuper = unfold(M=M, wavecar='WAVECAR', lsorbit=True)
cell = [[0, 3.03, 3.03],
        [3.03, 0, 3.03],
        [3.03, 3.03, 0]]
kpts = [[1, 0.5, 0.5],            # X
        [0.0, 0.0, 0],            # G
        [1, 0.5, 0.5]]            # X
kpath = make_kpath(kpts, nseg=30)
sw = WaveSuper.spectral_weight(kpath)
# show the effective band structure with scatter
EBS_scatter(kpath, cell, sw, nseg=30, eref=float(fermi), ylim=(-5, 0),
            kpath_label=['X', 'G', 'X'], factor=100, color='C0')
