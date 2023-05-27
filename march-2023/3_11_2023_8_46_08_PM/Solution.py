# https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)
        n = len(s)
        i, j = 0, 0
        res = 0
        mx = 0
        while j < n:
            sm = j - i
            if dic:
                mx = max(dic.values())
            if sm - mx <= k:
                res = max(res, sm)
                dic[s[j]] += 1
                j += 1
            elif sm - mx > k:
                dic[s[i]] -= 1
                i += 1
        if dic:
            mx = max(dic.values())
        if j - i - mx <= k:
            res = max(res, j - i)
        return res
                