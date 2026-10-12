class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        ans = 0
        p = 0
        while i < len(s):
            if s[i] == '(':
                p += 1
            else:
                if p > 0:
                    p -= 1
                    if i + 1 < len(s) and s[i + 1] == ')':
                        i += 1
                    else:
                        ans += 1
                else:
                    if i + 1 < len(s) and s[i + 1] == ')':
                        ans += 1
                        i += 1
                    else:
                        ans += 2
            i += 1
        return ans + (p * 2)