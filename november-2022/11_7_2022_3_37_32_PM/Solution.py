# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

class Solution:
  def longestPalindrome(self, words: List[str]) -> int:

    c = Counter(words)
    res = 0

    for s in c:
      while (s!=s[1]+s[0] and s[1]+s[0] in c and c[s[1]+s[0]]>0 and c[s]>0) or (s[1]+s[0]==s and c[s]>=2):
        res += 4
        c[s] -= 1
        c[s[1]+s[0]] -= 1
    
    for s in c:
      if s[0] == s[1] and c[s] > 0:
        res += 2
        break

    return res