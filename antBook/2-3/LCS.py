'''
 Longest Common Subsequence (最長共通部分和)
 ex) S: abcd, T:becdのとき、LCS=3 ('bcd')

'''

import numpy as np 

def solve():
  S, T = init_problem()
  i = len(S)
  j = len(T)
  dp = np.zeros((i+1, j+1))
  for x in range(i):
    for y in range(j):
      if S[x] == T[y]:
        dp[x+1, y+1] = dp[x, y] + 1
      else:
        dp[x+1, y+1] = max(dp[x, y+1], dp[x+1, y])
  
  print(dp)
  return dp


def init_problem():
  S = ['a', 'b', 'c', 'd']
  T = ['b', 'e', 'c', 'd']
  return S, T


if __name__=='__main__':
  solve()

