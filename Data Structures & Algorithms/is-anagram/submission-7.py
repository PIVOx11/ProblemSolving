
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = {}, {}
        for x in range(len(s)):
            s_map[s[x]] = 1 + s_map.get(s[x], 0)
            t_map[t[x]] = 1 + t_map.get(t[x], 0)
        for c in s:
            if s_map[c] != t_map.get(c, 0):
                return False
        return True









