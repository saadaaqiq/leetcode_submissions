# https://leetcode.com/problems/find-the-original-array-of-prefix-xor

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i-1] ^ pref[i])
        return arr