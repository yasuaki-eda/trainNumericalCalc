import numpy as np
import matplotlib.pyplot as plt
import math

def test01():
  q1 = (1, 1, -1)  # (x, y, q)
  q2 = (3, 1, -1.5) 
  x0 = (0, 0)
  v0 = (1, 0)
  k = 1
  m = 1

  def F(_x, _q):
    r = math.sqrt( (_x[0] - _q[0])**2 + (_x[1] - _q[1])**2 )
    fx = (_x[0]-_q[0])/r * k * _q[2]/r**2
    fy = (_x[1]-_q[1])/r * k * _q[2]/r**2
    return fx, fy
  
  h = 0.01
  end_time = 30
  t = 0
  vx, vy = v0[0], v0[1]
  xx, xy = x0[0], x0[1]
  t_list = np.array([t])
  x_list = np.array([xx])
  y_list = np.array([xy])

  while t < end_time:
    t += h
    t_list = np.append(t_list, t)
    fx1, fy1 = F((xx,xy), q1)
    fx2, fy2 = F((xx,xy), q2)
    vx += (fx1+fx2)/m * h
    vy += (fy1+fy2)/m * h
    xx += vx*h
    xy += vy*h
    x_list = np.append(x_list, xx)
    y_list = np.append(y_list, xy)
  
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(x_list, y_list)
  ax.plot(q1[0], q1[1], marker='*', markersize=5, label='Q1')
  ax.plot(q2[0], q2[1], marker='*', markersize=5, label='Q2')
  ax.legend()
  plt.show()


if __name__ == '__main__':
  test01()
