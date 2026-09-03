class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for cs, ct in zip(s, t):
            if cs not in s_map:
                s_map[cs] = ct
            if ct not in t_map:
                t_map[ct] = cs
            if s_map[cs] != ct or t_map[ct] != cs:
                return False
        return True