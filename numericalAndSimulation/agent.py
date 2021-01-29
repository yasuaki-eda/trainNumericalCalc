import numpy as np
import matplotlib.pyplot as plt


class Agent:
  def __init__(self, category, x=0, y=0, dx=0, dy=1):
    self.x = 0
    self.y = 0
    self.dx = 0
    self.dy = 1
    self.category = category

  def calcnext(self):
    if self.category == 0:
      self.cat0()
    elif self.category == 1:
      self.cat1()
    else :
      print('categoryの指定が誤っています')

  def cat0(self):
    self.x += self.dx
    self.y += self.dy
    self.dx = 1 if self.dx==0 else 0
    self.dy = 1 if self.dy==0 else 0
  
  def cat1(self):
    self.x += self.dx
    self.y += self.dy
    self.dx = (np.random.random() - 0.5) * 2
    self.dy = (np.random.random() - 0.5) * 2

  def putstate(self):
    print('x:', self.x, 'y:', self.y, 'dx:', self.dx, 'dy:',self.dy)

def test_Agent():
  a = Agent(0)
  a.putstate()
  fig = plt.figure()
  ax = fig.add_subplot(111)
  xlist = []
  ylist = []
  for i in range(100):
    a.calcnext()
    a.putstate()
    xlist.append(a.x)
    ylist.append(a.y)
    plt.clf()
    plt.axis([0, 60, 0, 60])
    plt.plot(xlist, ylist, ".")
    plt.pause(0.01)
    xlist.clear()
    ylist.clear()
  plt.show()

def test_Agentcat1():
  a = Agent(1, dy=0)
  b = Agent(1, dy=0)
  for i in range(100):
    a.calcnext()
    b.calcnext()
    plt.clf()
    plt.axis([-50, 50, -50, 50])
    plt.plot([a.x], [a.y], ".")
    plt.plot([b.x], [b.y], "x")
    plt.pause(0.01)

  plt.show()

if __name__ == '__main__':
#  test_Agent()
  test_Agentcat1()

  
