#Enter a vector b and find the projection of b orthogonal to a given vector u
import numpy as np
def oprojection(of_vec, on_vec):
    x1 = np.array(of_vec)
    x2 =np.array(on_vec)
    scal = np.dot(x2, x1)/np.dot(x2, x2)
    vec = scal*x2
    return round(scal,10), np.around(vec, decimals =10)
print(oprojection([2,0,2,0],[1,0.0,0,1]))
print(oprojection([2,0,2,0],[6,0,2,0]))
print(oprojection([1,0,-2],[1,2,3]))