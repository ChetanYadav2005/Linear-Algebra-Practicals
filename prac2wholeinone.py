import numpy as np
u=[]
i=0
n=int(input("enter the total elements "))
while(i<n):
    x=int(input("enter an integer number: "))
    u.append(x)
    i=i+1
print(u)
v=[]
i=0
while(i<n):
    y=int(input("enter an integer number: "))
    v.append(y)
    i=i+1
print(v)
a=int(input("value of a: "))
b=int(input("value of b: "))

resultofu=[]
for item in u:
    resultofu.append(item * a)

resultofv=[]
for item in v:
    resultofv.append(item * b)

res_list = []
for i in range(0, len(resultofu)):
    res_list.append(resultofu[i] + resultofv[i])

c=(a*u)+(b*v)
d=np.dot(u,v)
print("ax+by vector is " ,res_list)
print("dot product is ",d)