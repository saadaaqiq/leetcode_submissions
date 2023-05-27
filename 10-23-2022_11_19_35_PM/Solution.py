# https://leetcode.com/problems/read-n-characters-given-read4

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
  def read(self, buf, n):
    temp = ['']*4    
    k = 0
    while k < n: 
      r = read4(temp)
      if r==0:
        break
      r = min(r, n-k)  
      buf[k:] = temp[:r]  
      k += r
    return k
  
  

        