class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        ans = []
        s = 0
        for i in d:
            s = (s * 10) + i
        s += 1
        while s:
            ans.insert(0, s % 10)
            s //= 10
        
        return ans