# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            s = "".join(sorted(string))
            if s not in dic:
                dic[s] = []
            dic[s].append(string)
        return list(dic.values())