# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        for i, s in enumerate(strs):
            arr.append((''.join(sorted(s)), i))
        arr.sort()
        print(arr)
        res = []
        i = 0
        while i < len(strs):
            j = i + 1
            temp = [strs[arr[i][1]]]
            while j < len(strs) and arr[j][0] == arr[i][0]:
                temp.append((strs[arr[j][1]]))
                j += 1
            i = j
            res.append(temp)
        return res

            
        