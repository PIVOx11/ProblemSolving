class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        ans = []
        C = {"1":0}
        for r in range(len(s)):
            if s[r] == "1":
                C["1"] += 1
            if l < len(s) and s[l] == "0":
                l += 1
            
            if C["1"] == k:
                ans.append(s[l:r + 1])
                while l < len(s) and (C["1"] == k or s[l] == "0"):
                    if s[l] == "1":
                        C["1"] -= 1
                    l += 1
        if not ans:
            return ""
        
        ans = sorted(ans, key=lambda x: len(x))
        l = len(ans[0])
        ans = sorted(list(filter(lambda x: len(x) == l, ans)))


        return ans[0]
            