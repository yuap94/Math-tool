#The Schimidt orthogonalizytion is follow by https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process
__author__ = "yuap94"
__date__ = "$28-May-2019$"

import numpy as np

def SO(matrix): #Schimidt orthogonalizytion with normalization
    def proj(v,u): # input should be np array
        return (np.dot(v,u)/np.dot(u,u)) * u
    
    (n,m) = matrix.shape
    o_matrix = matrix.T
    o_matrix[0] = o_matrix[0] / np.sum(o_matrix[0])
    for i in range(1,m):
        sum_proj = np.zeros(n)
        for k in range(1,i+1):
            sum_proj = sum_proj + proj(o_matrix[i],o_matrix[k-1])
        o_matrix[i] = o_matrix[i]-sum_proj
        o_matrix[i] = o_matrix[i] / np.sum(o_matrix[i])
        
    return o_matrix.T

ex_matrix = np.array([[1,2,4],[0,0,5],[0,3,6]])
print(SO(ex_matrix))