class Solution:
    def compress(self, s: List[str]) -> int:
        i = j = 0
        l = len(s)
        n = 0
        while j <= l:
            if j == l or s[i] != s[j]:
                i += 1
                if n > 1:
                    for x in str(n):
                        s[i]=x
                        i += 1
                n = 0
                if j < l:
                    s[i] = s[j]
            j += 1
            n += 1


        print("".join(s))
        return i