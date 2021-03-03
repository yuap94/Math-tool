import numpy as np

def rot_mat(axis, theta): 
    """
    WIKI:Euler–Rodrigues formula
    axis: rotation axis (3D)
    theta: the rotated angle, in radius
    """
    axis = axis / np.linalg.norm(axis)
    #Euler parameters: a, b, c, d
    a = np.cos(theta / 2.)
    b,c,d = axis * np.sin(theta / 2.)
    aa, bb, cc, dd = a**2, b**2, c**2, d**2
    ab, ac, ad, bc, bd, cd = a*b, a*c, a*d, b*c, b*d, c*d
    return np.array([[aa + bb - cc - dd, 2 * (bc - ad), 2 * (bd + ac)],
                     [2 * (bc +ad), aa + cc- bb - dd, 2 * (cd - ab)],
                     [2 * (bd - ac), 2 * (cd + ab), aa + dd - bb - cc]])
  
  
#example
vec = [3, 4, 5]
axis = [1, 0, 0]
theta = np.pi / 2
vec_out = rot_mat(axis, theta) @ v
