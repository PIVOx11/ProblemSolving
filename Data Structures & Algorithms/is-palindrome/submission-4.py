class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        l = []
        for i, c in enumerate(s):
            if not c.isalnum() or c.isspace():
                l.append(i)
        s = [value for i, value in enumerate(s) if i not in l]
        return s == s[::-1]
