def helper(s: str):
    res = ""
    i = 0
    l = len(s)
    
    while i < l:
        c = s[i]
        count = 0
        j = i
        while j < l and s[j] == c:
            count += 1
            j += 1
        i = j
        res += f"{str(count)}" + c

    return res

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            s = helper(s)
        return s