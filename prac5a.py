#Write a program to convert a matrix into its row echelon form:
def RE (M):
  if not M: return
  lead = 0
  rowcount = len(M)
  columncount = len(M[0])
  for r in range(rowcount):
    if lead >= columncount:
      return
    i = r
    while M[i][lead] == 0:
      i += 1
      if i == rowcount:
        i = r
        lead += 1
        if columncount == lead:
          return
    M[i],M[r] = M[r], M[i]
    lv = M[r][lead]
    M[r]= [mrx /float(lv) for mrx in M[r]]
    for i in range (rowcount):
       if i!=r:
         lv = M[i][lead]
         M[i]= [iv-lv*rv for rv, iv in zip(M[r],M[i])]       
         lead += 1
mtx = [[1,5,10],[2,6,10],[3,8,10],[4,12,20]]
RE(mtx)
for rw in mtx:
       print(','.join((str(rv)for rv in rw))) 