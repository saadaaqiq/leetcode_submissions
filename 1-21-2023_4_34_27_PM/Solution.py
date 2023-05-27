# https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        curr = []

        def backtrack(i):
            if i == len(s):
                if len(curr) == 4:
                    ip_str = ".".join(["".join(w) for w in curr])
                    res.append(ip_str)
                return
            if len(curr)<4:
                curr.append([s[i]])
                backtrack(i+1)
                curr.pop()
            if curr and len(curr)<=4 and int("".join(curr[-1])) != 0 and int("".join(curr[-1]) + s[i]) <= 255:
                curr[-1].append(s[i])
                backtrack(i+1)
                curr[-1].pop()
            return 

        backtrack(0)

        return res
                