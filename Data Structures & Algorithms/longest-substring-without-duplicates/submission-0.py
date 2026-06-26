class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set() #sub(w) r = 2, l = 1 longest = 2
        longest = 0
        l = 0
        r = 0
        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            longest = max(longest, len(sub))
            r += 1
        return longest