# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.translate(s.maketrans('', '', string.punctuation)).lower().replace(" ", "")
        i,j = 0, len(st)-1
        print(st)
        while i<j:
            if st[i] != st[j]:
                return False
            else:
                i+=1
                j-=1
        
        return True