class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, c in enumerate(s, start=1):
            ans += (123 - ord(c)) * i
        
        return ans