import numpy as np
from matplotlib import pyplot as plt
import math

def geometric_Pr(p=0.3, k=5):
  p = 1 if p<0 or 1<=p else p
  q = 1-p
  return q**(k-1)*p

def binomial_Pr(p=0.3, n=10, k=3):
  if n <0 or n<k:
    return 0
  p = 1 if p<0 or 1<=p else p
  q = 1-p
  coeff = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
  return coeff*p**k*q**(n-k)

def show_binomial(p=0.3, n=10):
  x = []
  for k in range(1, n+1):
    x.append(binomial_Pr(p, n, k))

  fig = plt.figure()
  title = 'binomial distribution p='+str(p)+' n='+str(n)
  ax = fig.add_subplot(111, title=title)
  ax.bar(range(1, n+1), x)
  plt.show()  

def show_geometric(p=0.3, kmax=15):
  x = []
  for k in range(1, kmax):
    x.append(geometric_Pr(p=p, k=k))

  fig = plt.figure()
  ax = fig.add_subplot(111, title='test !!', xlim=(0.5,kmax))
  ax.bar(range(1,kmax), x)
  plt.title('geometric distribution p=' + str(p))
  plt.show()


if __name__ == '__main__':
#  show_geometric()
  show_binomial(p=0.2, n=20)


