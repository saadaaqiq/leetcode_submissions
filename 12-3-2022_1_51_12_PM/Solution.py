# https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return "".join(sorted([c*count[c] for c in count], reverse=True, key=lambda x:len(x)))