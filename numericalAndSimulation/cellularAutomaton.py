import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

'''
  1次元セルオートマトン
  きれいに表示されるR : R = np.array([0,1,0,0,1,0,0,0])
'''
def CA_1d(s=128, tmax=128):
#  np.random.seed(1)
  img = np.zeros((tmax, s))
  R = np.random.randint(0, 2, (8))  # rule
#  R = np.array([0,1,0,0,1,0,0,0])
  print( 'Rule:',R)
  img[0, :] = np.random.randint(0, 2, (s))

  t = 0
  while t < tmax-1:
    t += 1
    img0 = np.copy(img[t-1, :])
    i0 = img0[:s-2]
    i1 = img0[1:s-1]
    i2 = img0[2:s]
    img[t, 1:s-1] = R[(4*i0 + 2*i1 + i2).astype(np.uint8)]

  fig = plt.figure()
  plt.imshow(img)
  plt.show()

def calc_CA_id(s=128, tmax=128):
  img = np.zeros((tmax, s))
  R = np.random.randint(0, 2, (8))  # rule
  img[0, :] = np.random.randint(0, 2, (s))

  t = 0
  while t < tmax-1:
    t += 1
    img0 = np.copy(img[t-1, :])
    i0 = img0[:s-2]
    i1 = img0[1:s-1]
    i2 = img0[2:s]
    img[t, 1:s-1] = R[(4*i0 + 2*i1 + i2).astype(np.uint8)]
  return img

# import matplotlib.animationを使わないとうまくいかない
def movie_CA1d():
  N = 100
  fig, ax = plt.subplots()
  def update(i):
    img = calc_CA_id()
    plt.clf()
    plt.imshow(img)
  hoge = ani.FuncAnimation(fig, update, np.arange(1,  N), interval=50)  # 代入しないと消される
  plt.show()

if __name__ == '__main__':
#  CA_1d()
  movie_CA1d()
