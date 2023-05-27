# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i,j = 0,0
        maxi,count = 0,0
        
        while j < len(s):
            if (s[j] not in dic) or (s[j] in dic and dic[s[j]]<i):
                dic[s[j]] = j
                count += 1
                j += 1
                maxi = max(maxi, count)
            else:
                i = dic[s[j]] + 1
                dic[s[j]] = j
                count = j - i + 1
                j += 1
        
        return maxi