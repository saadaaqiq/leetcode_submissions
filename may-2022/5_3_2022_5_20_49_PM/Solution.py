# https://leetcode.com/problems/group-anagrams

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        d = {}
        res = []
        
        for i in range(len(strs)):
            stri = "". join(sorted(strs[i]))
            if stri not in dic:
                dic[stri] = i
            p = dic[stri]
            
            if p not in d:
                d[p] = []
            d[p] += [i]
            
        for k in d:
            l = []
            for i in d[k]:
                l.append(strs[i])
            res.append(l)
        
        return res