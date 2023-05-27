# https://leetcode.com/problems/decode-xored-array

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        n = len(encoded) + 1
        for i in range(n-1):
            res.append(res[-1]^encoded[i])
        return res


