# https://leetcode.com/problems/fizz-buzz

class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    res = [str(i+1) for i in range(n)]
    i, j = 2, 4
    while i < n: 
      res[i] = "Fizz"
      i += 3
    while j < n: 
      res[j] = "Buzz" if res[j] != "Fizz" else "FizzBuzz"
      j += 5
    return res
    