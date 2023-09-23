import numpy as np
def oprojection(of_vec, on_vec):
    v1=np.array(of_vec)
    v2=np.array(on_vec)
    scal= np.dot(v2,v1) /np.dot(v2,v2)
    vec=scal*v2
    return round(scal,10),np.around(vec, decimals=10) #Create an orthonormal basis.

vl=[-2.0,-3.0,-2.0]
v2=[2.0,-4.0,-1.0] 
x=[-4.0,-2.0,1.0]

def make_unit_vec(u):
    import numpy as np
    bottom=np.linalg.norm(u)
    return u/bottom

b1= make_unit_vec([-2.0,-3.0,-2.0])
print(b1)
print (oprojection(v2, b1))
v2_perp=v2-oprojection(v2, b1)[1]
b2=make_unit_vec(v2_perp)
print (b2)
print ("Check whether b1 and b2 are orthogonal or not ")
print (np.linalg.norm(b2))
print(np.dot(b1,b2))

#Projection of onto newly formed orthonormal basis
P1= np.outer(b1,b1)
print (P1)
P2=np.outer(b2,b2) 
print(P2)
P=P1+P2 #Final projection matrix
print(P)
t = np.dot(P,x)
print(t)
tp=x-t 
print(tp)