import numpy as np
import matplotlib.pyplot as plt

def test01():
  end_time = 20
  h = 0.01
  x0 = 100
  g = -9.8
  v0 = 10
  t = 0
  list_t = np.array([])
  list_x = np.array([])

  while (t < end_time):
    t = t + h
    list_t = np.append(list_t, t)
    v = g*t + v0
    x = 1/2*g*t*t + v*t + x0
    list_x = np.append(list_x, x)
    if x < 0:
      break
  
#  plt.plot(list_t, list_x)
#  plt.show()
  return list_t, list_x


def test02():
  end_time = 20
  h = 0.01
  x0 = 100
  g = -9.8
  v0 = 10
  t = 0
  list_t = np.array([])
  list_x = np.array([])

  while(t< end_time):
    t = t + h
    list_t = np.append(list_t, t)
    v = g * h + v0
    x = v * h + x0
    list_x = np.append(list_x, x)
    v0 = v
    x0 = x
    if x < 0:
      break
  return list_t, list_x
  
#  plt.plot(list_t, list_x)
#  plt.show()

def test03():
  t1, x1 = test01()
  t2, x2 = test02()
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(t1, x1, label='test01')
  ax.plot(t2, x2, label='test02')
  ax.legend()
  plt.show()

def test04():
  end_time = 20
  rk = free_fall_RK(-9.8, 10, 100, 0.01, end_time)
  while (rk.t < end_time):
    rk.forward()
    if rk.x < 0:
      break
  rk.show_result()

def test05():
  rk = free_fall_RK(-9.8, 10, 100, 0.01, 20)
  rk.compute()
  t1, x1 = test01()
  t2, x2 = test02()
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(t1, x1, label='test01')
  ax.plot(t2, x2, label='test02')
  ax.plot(rk.t_list, rk.x_list, label='RK')
  ax.legend()
  plt.show()


# runge_kutta
class free_fall_RK():
  def __init__(self, g, v0, x0, h, endtime):
    self.g = g
    self.h = h
    self.x = x0
    self.v = v0
    self.t = 0
    self.endtime = endtime
    self.t_list = np.array([])
    self.x_list = np.array([])

  def compute(self):
    while (self.t < self.endtime):
      self.forward()
      if self.x < 0:
        break


  def dvdt(self, v, t):
    return self.g

  def dxdt(self, x, t):
    return self.v
  
  def forward(self):
    self.t += self.h
    
    self.t_list = np.append(self.t_list, self.t)
    vk1 = self.h * self.dvdt(self.v, self.t)
    vk2 = self.h * self.dvdt(self.v+self.h/2, self.t+vk1/2)
    vk3 = self.h * self.dvdt(self.v+self.h/2, self.t+vk2/2)
    vk4 = self.h * self.dvdt(self.v+self.h, self.t+vk3)
    self.v = self.v + vk1/6 + vk2/3 + vk3/3 + vk4/6
        
    xk1 = self.h * self.dxdt(self.x, self.t)
    xk2 = self.h * self.dxdt(self.x+self.h/2, self.t+xk1/2)
    xk3 = self.h * self.dxdt(self.x+self.h/2, self.t+xk2/2)
    xk4 = self.h * self.dxdt(self.x+self.h, self.t+xk3)
    self.x = self.x + xk1/6 + xk2/3 + xk3/3 + xk4/6
    self.x_list = np.append(self.x_list, self.x)

  def show_result(self):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    print(self.x, self.t)
    ax.plot(self.t_list, self.x_list, label='RK')
    ax.legend()
    plt.show()

if __name__ == '__main__':
  test05()



