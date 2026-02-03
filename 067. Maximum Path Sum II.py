import numpy as np
N = 100
  
def maxPathSum(tri, i, j, row, col, PATHS_LEN): 
    if(j == col): 
        return 0
    if(i == row-1): 
        return tri[i][j]
    if PATHS_LEN[i][j] == 0:
        PATHS_LEN[i][j]= max(maxPathSum(tri, i+1, j, row, col, PATHS_LEN), maxPathSum(tri, i+1, j+1, row, col, PATHS_LEN))
    return tri[i][j] + PATHS_LEN[i][j]
PATHS_LEN=np.zeros((N,N), dtype=int)
tri=np.zeros((N,N), dtype=int)
for i in range(N):
    #triangle is the file where i copied the triangle
    l=np.loadtxt("triangle.txt", dtype=int, usecols=i, skiprows=i)
    if l.size!=1:
        for j in range(l.size):
            tri[j+i][i]=l[j]            
    else:
        tri[i][i]=l
            
print(maxPathSum(tri, 0, 0, N, N, PATHS_LEN)) 

