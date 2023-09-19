import matplotlib.pyplot as plt
s= { 3+3j, 4+3j, 2+1j, 5+1j, 2+ 1j}
angle = int(input("enter angle rotation: "))
if angle == 90 :
    s1 = {x*1j for x in s}
    print(s1)
    X = [x.real for x in s1]
    Y =[x.imag for x in s1 ]
    plt.plot(X,Y, 'ro')
    plt.axis([-6,6,-6,6])
    plt.show()
elif angle == 180 : 
      s1={x*-1 for x in s}
      print(s1)
      X = [x.real for x in s1]
      Y = [ x.imag for x in s1]
      plt.plot(X,Y, 'ro')
      plt.axis([-6,6,-6,6])
      plt.show()
else:
      print("invalid angle ")
