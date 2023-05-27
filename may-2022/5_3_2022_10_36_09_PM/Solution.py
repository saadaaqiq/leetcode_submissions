# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            arr = [0 for i in range(26)]
            for c in strs[i]:
                arr[ord(c)-97] += 1
            arrStr = str(arr)
            if arrStr not in dic:
                dic[arrStr] = []
            dic[arrStr].append(strs[i])
        
        return list(dic.values())
            
