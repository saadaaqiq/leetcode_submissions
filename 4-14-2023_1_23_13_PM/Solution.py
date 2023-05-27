# https://leetcode.com/problems/strobogrammatic-number

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        s = [c for c in str(num)]
        n = len(s)
        dic = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}

        if n%2 and s[n//2] not in ["0", "1", "8"]:
            return False
                
        arr1 = s[:n//2]
        arr2 = s[n//2 + n%2:]
        
        for c in arr2:
            if not arr1 or c not in dic or arr1[-1] != dic[c]:
                return False
            arr1.pop()

        return True