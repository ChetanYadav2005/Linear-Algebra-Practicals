#Program to find the inverse of invertible matrix
import numpy as  np
M = ([[1,2,1],[2,1,0],[3,0,2]])
print("the matrix M is:",M)
a = np.linalg.det(M)
print("Determinant of matrix M is", a)
if a !=0: 
    Minv = np.linalg.inv(M)
    print("The inverse of matrix M is:", Minv)
else:
    print("matrix is not invertible")
