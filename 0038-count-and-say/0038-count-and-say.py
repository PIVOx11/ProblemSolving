
def say(arr: list):
    s = ""
    for ar in arr:
        s += f"{str(ar[0])}{ar[1]}"
    return s

def count(s: str):
    res = []
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
        res.append([count, c])
    return res

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            s = say(count(s))
        return s