from unfold import make_kpath, removeDuplicateKpoints, find_K_from_k, save2VaspKPOINTS
import numpy as np

# The tranformation matrix between supercell and primitive cell.
M = [[0.,  1., -1., ], [1., -1.,  0.], [-9., -9., -9.]]
# high-symmetry point of a Hexagonal BZ in fractional coordinate
kpts = [[1, 0.5, 0.5],            # X
        [0.0, 0.0, 0],            # G
        [1, 0.5, 0.5]]            # X
# create band path from the high-symmetry points, 30 points inbetween each pair of high-symmetry points
kpath = make_kpath(kpts, nseg=30)
K_in_sup = []
for kk in kpath:
    kg, g = find_K_from_k(kk, M)
    K_in_sup.append(kg)
# remove the duplicate K-points
reducedK = removeDuplicateKpoints(K_in_sup)

# save to VASP KPOINTS
save2VaspKPOINTS(reducedK)
