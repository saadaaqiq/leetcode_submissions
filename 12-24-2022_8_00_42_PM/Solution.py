# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
  def numTilings(self, n: int) -> int:

    MOD = 1_000_000_007

    @cache
    def fullCover(k):
      if k <= 2:
        return k
      return (fullCover(k-1) + fullCover(k-2) + 2 * partialCover(k-1)) % MOD

    @cache
    def partialCover(k):
      if k == 2:
        return 1
      return (partialCover(k-1) + fullCover(k-2)) % MOD
    
    return fullCover(n) % MOD
      

