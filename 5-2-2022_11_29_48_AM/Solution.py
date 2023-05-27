# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        punct = set(string.punctuation)
        punct.add(" ")
        sl = list(s)
        
        i=0
        j=0
        while j < len(sl):
            if sl[j] not in punct:
                sl[i] = sl[j].lower()
                i+=1
                j+=1
            else:
                j+=1
                
        if len(sl) == 1:
            return True
        
        k = 0
        l = i-1
        while k<l:
            if sl[k] != sl[l]:
                return False
            else:
                k+=1
                l-=1
        
        return True