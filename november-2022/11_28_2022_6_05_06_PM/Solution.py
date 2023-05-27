# https://leetcode.com/problems/count-palindromic-subsequences

class Solution:
  def countPalindromes(self, string: str) -> int:
    res = 0 
    mod = 10**9 + 7
    def prefFunction(s):
      n = len(s)
      pref = [[0]*10 for _ in range(n+1)]
      ppref = [[0]*100 for _ in range(n+1)]
      for k in range(1,n+1):
        for j in range(10):
          pref[k][j] = pref[k-1][j]
        for j in range(100):
          ppref[k][j] = ppref[k-1][j]
        d = int(s[k-1])
        for j in range(10):
          ppref[k][10*j + d] += pref[k-1][j]
        pref[k][d] += 1
      return ppref

    ppref = prefFunction(string)
    ssuf  = list(reversed(prefFunction(list(reversed(string)))))

    res = 0
    for k in range(1, len(string)+1):
      for j in range(100):
        res += ppref[k-1][j] * ssuf[k][j] % mod
    return res % mod
    

      

    
