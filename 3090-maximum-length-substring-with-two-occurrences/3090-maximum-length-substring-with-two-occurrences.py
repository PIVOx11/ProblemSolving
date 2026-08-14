class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        charCount = defaultdict(int)
        l = 0
        ans = 0

        for right in range(len(s)):
            charCount[s[right]] += 1
        

            while charCount[s[right]] > 2:
                charCount[s[l]] -= 1
                l += 1
            ans = max(right - l + 1, ans)
        
        return ans

