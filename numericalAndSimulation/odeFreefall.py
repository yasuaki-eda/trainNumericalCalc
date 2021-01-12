import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

G = 9.80665  #重力加速度
def f(x, t):
  return[x[1], -G]

v = float(input('初速を入力：'))
x = float(input('初期高さを入力:'))

x0 = [x, v]
t = np.arange(0, 4.53, 0.01)
x = odeint(f, x0, t)
#print(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t, x[:,0])
plt.show()


