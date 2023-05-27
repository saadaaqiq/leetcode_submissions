# https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dic = {}
        i=0
        maxi=0
        result = 0
        
        for j in range(len(s)):
            dic[s[j]] = 1 + dic.get(s[j], 0)
            maxi = max(maxi, dic[s[j]])
            while (j-i+1) - maxi > k:
                dic[s[i]] -= 1
                i+=1
            result = max(result, j-i+1)
               
        return result
                