#Rotation by 90 deg
import matplotlib.pyplot as  plt
x = 2+2j
z = 1j
plt.scatter(x.real, x.imag, color = 'red')
c =x*z
plt.scatter(c.real, c.imag)
plt.show()