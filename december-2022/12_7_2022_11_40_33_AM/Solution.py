# https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, a: str, b: str) -> bool:
        return not (len(a) != len(b) or set(a) != set(b)) and sorted(list(Counter(a).values())) == sorted(list(Counter(b).values()))
        