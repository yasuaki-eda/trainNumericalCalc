import numpy as np
import random
import math

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

if __name__ =='__main__':
#  linear_congruential_generator()
#  python_random()
#  test_trape()
  test_ri()


