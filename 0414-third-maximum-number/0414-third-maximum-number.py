class Solution:
    def thirdMax(self, n: list[int]) -> int:
        # First Idea
        # n = sorted(list(set(n)))

        # return n[-3] if len(n) >= 3 else max(n)
        if len(set(n)) < 3:
            return max(n)
        elif len(set(n)) == 3:
            return min(n)
        
        t = max(n)
        s = f = -float("inf")
        n = set(n)

        for n in n:
            if n > f:
                f, s, t = n, f, s
            elif n > s:
                s, t = n, s
            elif n > t:
                t = n
        
        return t



