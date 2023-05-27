# https://leetcode.com/problems/fizz-buzz

class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    res = [str(i+1) for i in range(n)]
    i, j, k = 2, 4, 14
    while i < n: 
      res[i] = "Fizz"
      i += 3
    while j < n: 
      res[j] = "Buzz"
      j += 5
    while k < n:
      res[k] = "FizzBuzz"
      k += 15
    return res
    