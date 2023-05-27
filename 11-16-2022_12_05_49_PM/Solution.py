# https://leetcode.com/problems/reorganize-string

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = []
        for c in count:
            heapq.heappush(h, (-count[c], c))
        res = ""
        while h:
            k, c = heapq.heappop(h)
            if not res or res[-1] != c:
                res += c
                k += 1
                if k < 0:
                    heapq.heappush(h, (k, c))
            else:
                if not h:
                    return ""
                else:
                    kt, ct = heapq.heappop(h)
                    heapq.heappush(h, (k, c))
                    res += ct
                    kt += 1
                    if kt < 0:
                        heapq.heappush(h, (kt, ct))
        return res

