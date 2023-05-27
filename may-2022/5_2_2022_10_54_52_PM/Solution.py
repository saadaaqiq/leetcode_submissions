# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        i=0
        result = 0
        for j in range(len(s)):
            while s[j] in st:
                st.remove(s[i])
                i+=1
            st.add(s[j])
            result = max(result, j-i+1)
        return result