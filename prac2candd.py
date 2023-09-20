#date:-7/7/23
#enter a vector u and v as an list 
#find the vector au+bv for different values of a and b 
#find the dot product of u and v

import numpy as np
#enter vector as as n-list
u=np.array([5,6,7])
v=np.array([1,2,3])
print(u)
print(v)
a=int(input("value of a: "))
b=int(input("value of b: "))
c=a*u+b*v
d=np.dot(u,v)
print("ax+by vector is " ,c)
print("dot product is ",d)
