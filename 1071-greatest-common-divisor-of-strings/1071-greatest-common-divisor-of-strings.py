class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        l1, l2 = len(s1), len(s2)
        ans = [""]
        for i in range(1, l2 + 1):
            part = s2[0: i]
            m1 , m2 = l1 // len(part), l2 // len(part)

            if part * m1 == s1 and part * m2 == s2:
                ans.append(part)
        return ans[-1]