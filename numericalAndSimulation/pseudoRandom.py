import numpy as np
import random
import math
import matplotlib.pyplot as plt

def linear_congruential_generator():
  m = 2**32
  a = 12664525
  c = 1013904223
  R0 = 10

  for i in range(10):
    R1 = (a*R0+c)%m
    print(R1)
    R0 = R1

def python_random():
  random.seed(1)
  for i in range(10):
#    x = random.random()
    x = random.randint(0, 4)
    print(x)

'''
 台形公式による4分円の面積計算
'''
def trapezoid_rule(x0, xn, fx, d=100):
  h = (xn - x0) / d
  S = 0
  x = x0
  while x <= xn:
    x1 = x+h
    S += (fx(x) + fx(x1)) /2 * h 
    x += h
  return S

def circle_1q(x):
  if x < 0 or x > 1:
    return 0
  return math.sqrt(1-x**2)

'''
  乱数生成による四分円の面積計算
'''
def ri(N=100000, phase=10):
  np.random.seed(0)
  res = np.zeros((phase))
  for p in range(phase):
    count_in = 0
    for n in range(N):
      rx = np.random.random()
      ry = np.random.random()
      if rx**2+ry**2 <= 1:
        count_in += 1
    res[p] = count_in / n
  
  return res

'''
  乱数によるナップザック問題の解析
'''
def random_knapsack(weight_limit=250, phase=10, cycle=100):
  baggage = np.array([
    [87, 66, 70, 25, 33, 24, 89,63, 23, 54],
    [96, 55, 21, 58, 41, 81, 8, 99, 59, 62]
  ])
  np.random.seed(3)
#  l = np.append(l, baggage[:,1].reshape(2,1), axis=1)

  for p in range(phase):
    value = 0
    good_list = []
    for c in range(cycle):
      list_baggage = np.zeros((2, 0))
      random_list = baggage[:, np.random.choice(baggage.shape[1], baggage.shape[1], replace=False)]
      weight = 0
      for r in range(random_list.shape[1]):
        tmp_weight = weight + random_list[0,r]
        if weight_limit <= tmp_weight:
          break
        weight += random_list[0,r]
        list_baggage = np.append(list_baggage, random_list[:,r].reshape(2,1), axis=1)
      if value <= np.sum(list_baggage[1,:]):
        value = np.sum(list_baggage[1,:])
        good_list = np.copy(list_baggage)
    print( 'value:', value, ' weight:', np.sum(good_list[0,:]), 'list:', good_list)

def random_walk(time_limit=1000):
  X = np.zeros((2,1))
#  np.random.seed(0)
  for t in range(time_limit):
    x = X[0,t] + (np.random.random() - 0.5) * 2
    y = X[1,t] + (np.random.random() - 0.5) * 2
    X = np.append(X, [[x],[y]], axis=1)
  
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(X[0,:], X[1,:])
  plt.show()


def test_trape():
  d = 10
  S = trapezoid_rule(0, 1, circle_1q, d=d)
  print('d:',d, ' S:', 4*S)
  d  = 50
  S = trapezoid_rule(0, 1, circle_1q, d=d)
  print('d:',d, ' S:', 4*S)
  d  = 100
  S = trapezoid_rule(0, 1, circle_1q, d=d)
  print('d:',d, ' S:', 4*S)
  d  = 10000
  S = trapezoid_rule(0, 1, circle_1q, d=d)
  print('d:',d, ' S:', 4*S)


def test_ri():
  p = 10
  res = ri(N=1000000, phase=p)
  print(res*4)

def test_knapsack():
  random_knapsack()

if __name__ =='__main__':
#  linear_congruential_generator()
#  python_random()
#  test_trape()
#  test_ri()
#  test_knapsack()
  random_walk(time_limit=1000)


