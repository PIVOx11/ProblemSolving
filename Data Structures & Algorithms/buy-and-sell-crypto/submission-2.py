class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        pre = p[0]

        for i in p[1:]:
            if i > pre:
                res = max(res, i  - pre)
                continue
            pre = i
        
        return res