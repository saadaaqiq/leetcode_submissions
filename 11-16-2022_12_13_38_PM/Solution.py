# https://leetcode.com/problems/distant-barcodes

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        h = []
        res = []
        for b in counter:
            heapq.heappush(h, (-counter[b], b))
        while h:
            count, code = heapq.heappop(h)
            if not res or code != res[-1]:
                res.append(code)
                count += 1
                if count < 0:
                    heapq.heappush(h, (count, code))
            else:
                newcount, newcode = heapq.heappop(h)
                heapq.heappush(h, (count, code))
                res.append(newcode)
                newcount += 1
                if newcount < 0:
                    heapq.heappush(h, (newcount, newcode))
        return res