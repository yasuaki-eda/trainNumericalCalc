'''
 動的計画法(DP)
 ナップサック問題
'''
import numpy as np

'''
 計算結果をテーブルに格納
'''
def solve_v1():
  N, wv, W = init_knapsak()
  table = np.ones((N+1, W+1)) * (-1)
  val = calc_v1(wv, 0, N, W, table)
  print(str(val))
  print(table)
  return

def calc_v1(wv, n, N, weight, table):
  if (n >= N):
    val = 0
  elif (wv[n, 0] > weight):
    val = calc_v1(wv, n+1, N, weight, table)
  else :
    if (table[n, weight] >= 0):
      val = table[n, weight]
    else :
      val = max(calc_v1(wv, n+1, N, weight, table), calc_v1(wv, n+1, N, weight - wv[n,0], table) + wv[n,1])
  table[n, weight] = val
  return val


'''
 全数探索
'''
def solve_v0():
  N, wv, W = init_knapsak()
  val = calc_v0(wv, 0, N, W)
  print(str(val))
  return

'''
 全数探索
'''
def calc_v0(wv, n, N, weight):
  if (n >= N):
    val = 0
  elif (wv[n, 0] > weight):
    val = calc_v0(wv, n+1, N, weight)
  else :
    val = max(calc_v0(wv, n+1, N, weight), calc_v0(wv, n+1, N, weight - wv[n,0]) + wv[n,1])
  return val


def init_knapsak():
  N = 4
  wv = [[2, 3],[1, 2],[3,4],[2,2]]
  W = 5
  return N, np.array(wv), W



if __name__ == '__main__':
  solve_v1()


