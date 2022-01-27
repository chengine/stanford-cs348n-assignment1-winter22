import numpy as np
from scipy.spatial.transform import Rotation as R

def rotate(points, rotation):
    r = R.from_euler('xyz', rotation, degrees=True)
    return r.as_matrix() @ points

def scale(points, size):
    ret = np.zeros(points.shape)
    for ind, pt in enumerate(points):
        ret[ind] = pt*size

    return ret

def compare_voxels(vx1, vx2):
    return np.count_nonzero(vx1==vx2)

def compare_pcs(pc1, pc2):
    n = pc1.shape[0]
    m = pc2.shape[1]

    sum1 = 0
    for a in range(n):
        norm_i = float('inf')
        p_i = pc1[a]
        for b in range(m):
            p_j = pc2[b]
            norms = np.linalg.norm(p_i - p_j)
            if norms < norm_i:
                norm_i = norms
        sum1 += norm_i

    sum2 = 0
    for c in range(m):
        norm_j = float('inf')
        p_j = pc2[c]
        for d in range(n):
            p_i = pc1[d]
            norms = np.linalg.norm(p_i - p_j)
            if norms < norm_j:
                norm_j = norms
        sum2 += norm_j

    return 0.5*(sum1/n + sum2/m)