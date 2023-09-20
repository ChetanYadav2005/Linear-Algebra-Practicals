#multiplication of two matrices
a=[[12,7,3],
    [4,5,6],
    [7,8,9]]
#take 3x4 matrix
b=[[5,8,1,2],
   [6,7,3,0],
   [4,5,9,1]]
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

#iteratiing by row of a
for i in range(len(a)):
    #iteerating by column b
    for j in range(len(b[0])):
        #ioterating rows of b
        for k in range(len(b)):
            result[i][j]+=a[i][k]*b[k][j]
for r in result:
    print(r)
