import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math


'''
 laplace方程式 d^2x + d^2y = 0
 ヤコビ法によるラプラス方程式の反復数値計算
 @param u : 境界条件を設定した点群(x, y, value). 中央は0で初期化済
 @param cycle : ループ数
'''
def laplace_jacobi_method(u, cycle=1000):
  h, w = u.shape
  u_out = np.copy(u)
  for c in range(cycle):
    u1 = u_out[:h-2, 1:w-1]
    u2 = u_out[1:h-1, :w-2]
    u3 = u_out[1:h-1, 2:w]
    u4 = u_out[2:h, 1:w-1]
    u_out[1:h-1, 1:w-1] = (u1+u2+u3+u4)/4
#    print(u1[10, :10], u1[:10,10])
  return u_out

'''
 poisson方程式 d^2x + d^2y = f(x,y)
 ヤコビ法によるラプラス方程式の反復数値計算
 @param u : 境界条件を設定した点群(x, y, value). 中央は0で初期化済
 @param f : 方程式右辺の関数(uを入力してu.shape形式で返す)
 @param h : 空間の刻み幅
 @param cycle : ループ数
'''
def poisson_jacobi_method(u, x, y, f, h=1, cycle=1000):
  H, W = u.shape
  u_out = np.copy(u)
  u5 = f(x, y)[1:H-1, 1:W-1]
  for c in range(cycle):
    u1 = u_out[:H-2, 1:W-1]
    u2 = u_out[1:H-1, :W-2]
    u3 = u_out[1:H-1, 2:W]
    u4 = u_out[2:H, 1:W-1]
    u_out[1:H-1, 1:W-1] = (u1+u2+u3+u4-h**2*u5)/4
#    print(u1[10, :10], u1[:10,10])
  return u_out

def test_poisson_jacobi():
  H, W = 100, 150
  u = np.zeros((H, W))
  X = np.array(range(H))
  Y = np.array(range(W))
  # 境界条件を設定
  u[0, :] = np.sin(Y/W*2*math.pi)
  u[:, 0] = 0
  u[H-1, :] = 0
  u[:, W-1] = 0
  
  def f(x, y):
    qx, qy=55.5, 100.3
    Q = 0.3
    k = 1
    xx, yy = np.meshgrid(x, y, indexing='ij')
    r = np.sqrt((xx - qx)**2+(yy-qy)**2)
#    u = np.zeros_like(xx)
    u = k * Q / r**2
    return u
  
  # 反復計算
  dst = poisson_jacobi_method(u, X, Y, f, h=1, cycle=100)

  # 結果の描画
  xx, yy = np.meshgrid(X, Y, indexing='ij')
  fig = plt.figure()
  ax = Axes3D(fig)
  ax.plot_surface(xx, yy, dst, cmap=cm.coolwarm)
  plt.show()


def test_laplace_jacobi():
  H, W = 100, 150
  u = np.zeros((H, W))
  X = np.array(range(H))
  Y = np.array(range(W))
  # 境界条件を設定
  u[0, :] = np.sin(Y/W*2*math.pi)
  u[:, 0] = np.cos(X/H*2*math.pi)
  u[H-1, :] = 1- Y/np.max(Y)
  u[:, W-1] = 0

  # 反復計算
  u_out = laplace_jacobi_method(u, cycle=1000)

  # 結果の描画
  XX, YY = np.meshgrid(X, Y, indexing='ij')
#  print(XX)
#  print(YY)
  print(XX.shape)
  print(YY.shape)
  fig = plt.figure()
  ax = Axes3D(fig)
  ax.plot_surface(XX, YY, u_out, cmap=cm.coolwarm)
  plt.show()


def gauss_v0(A, b):
  h, w = A.shape
  if h != w :
    print('AはN*N行列でなければなりません')
    return
  A1 = np.zeros((h, w+1), dtype=np.float32)
  A1[:, :w] = A
  A1[:, w] = b
  # 前進
  try :
    for x in range(h):
      if A1[x,x] != 0:
        A1[x, :] = A1[x, :]/A1[x, x]
      else:
        if np.all(A1[x, :w]==0):
          if A1[x, w] == 0:
            raise Exception('不定')
          else:
            raise Exception('解なし')
            
        for y in range(x+1, h):
          if A1[y,x] == 0:
            continue
          B = A1[x+1,:]
          A1[x+1, :] = A1[x, :]
          A1[x, :] = B
          break
        if A1[x,x] == 0:
          raise Exception('解なし')

      for y in range(x+1, h):
        A1[y, :] = A1[y, :] - A1[x, :] * A1[y, x]
    print(A1)
  except Exception as inst:
    print(inst)
  
  # 後退
  X = np.zeros((h))
  for x in range(h-1, 0, -1):
    X[x] = A1[x,w]
    A1[:x,w] -= A1[:x,x]*X[x]
    A1[:x,x] -= A1[:x,x]

  A2 = np.dot(A, X)
  print(A2)
  return X


def test_gauss_v0():
  A = np.array([
    [1, 2, 3, 4],
    [3, 4, 5, 4],
    [6, 5, 8, 7],
    [9, 10, 11, -10]
  ])
  b = np.array([[3, 5, 7, 9]])
  gauss_v0(A, b)

if __name__=='__main__':
#  test_gauss_v0()
#  test_laplace_jacobi()
  test_poisson_jacobi()


