# https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, a: str, b: str) -> bool:
        return set(Counter(a))==set(Counter(b)) and Counter(Counter(a).values()) == Counter(Counter(b).values())