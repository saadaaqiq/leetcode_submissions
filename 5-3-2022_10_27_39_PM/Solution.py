# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = []
        for s in strs:
            arr = [0 for i in range(26)]
            for c in s:
                arr[ord(c)-97] += 1
            lis.append("".join([(str(x)+",") for x in arr]))
        dic = {}
        for i in range(len(strs)):
            if lis[i] not in dic:
                dic[lis[i]] = []
            dic[lis[i]].append(strs[i])
        
        return list(dic.values())
            
