# https://leetcode.com/problems/fair-candy-swap

class Solution:
    def fairCandySwap(self, alice: List[int], bob: List[int]) -> List[int]:
        sa, sb = sum(alice), sum(bob)
        alice.sort()
        bob.sort()
        for a in alice:
            l, r = 0, len(bob)
            while l < r:
                mid = (l+r)//2
                if sa - a + bob[mid] < sb - bob[mid] + a:
                    l = mid + 1
                elif sa - a + bob[mid] > sb - bob[mid] + a:
                    r = mid
                else:
                    return [a, bob[mid]]