class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {"a", "i", "e", "o", "u"}
        ans = len([c for c in s[:k] if c in v])
        count = ans 
        left = 1
        right = k

        l = len(s)
        while right < l:
            if s[left - 1] in v:
                count -= 1
            
            if s[right] in v:
                count += 1
            
            ans = max(count, ans)
            left += 1
            right += 1
        return ans