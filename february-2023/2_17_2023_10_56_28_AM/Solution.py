# https://leetcode.com/problems/repeated-dna-sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        if len(s) < 10:
            return res
        counter = collections.Counter([s[:10]])

        for i in range(10, len(s)):
            p = s[i-9:i+1]
            counter[p] += 1
        for seq in counter:
            if counter[seq] > 1:
                res.append(seq)

        return res