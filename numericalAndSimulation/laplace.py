import numpy as np





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
  test_gauss_v0()
