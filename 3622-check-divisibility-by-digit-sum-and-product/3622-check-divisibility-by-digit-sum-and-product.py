class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        d = n
        p = 1

        while n:
            s, p = n % 10 + s, n % 10 * p
            n //= 10

        return d % (s + p) == 0