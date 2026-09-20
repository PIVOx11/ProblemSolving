class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        i = 1
        for c in s:
            ans += (123 - ord(c)) * i
            i += 1

        return ans
