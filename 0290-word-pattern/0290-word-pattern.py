class Solution:
    def wordPattern(self,p: str, s: str) -> bool:
        s = s.split()
        zi = set(zip(p, s))
        print(zi)
        return len(zi) == len(set(p)) and len(set(s)) == len(set(p)) and len(s) == len(p)