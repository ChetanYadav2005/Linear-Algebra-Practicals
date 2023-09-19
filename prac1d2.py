#Rotation by 180

import matplotlib.pyplot as plt
x = 2+2j
plt.scatter(x.real, x.imag, color = 'red')
plt.scatter(-1*x.real, -1*x.imag)
plt.show()
