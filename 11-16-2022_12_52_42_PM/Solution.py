# https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        self.arr = heapq.nlargest(k, nums)
        heapq.heapify(self.arr)

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
        else:
            if val > self.arr[0]:
                heapq.heappush(self.arr, val)
                heapq.heappop(self.arr)
        return self.arr[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)