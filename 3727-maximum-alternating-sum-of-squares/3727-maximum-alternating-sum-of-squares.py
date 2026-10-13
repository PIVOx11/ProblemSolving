class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = [i ** 2 for i in nums]
        n.sort()
        ranged = []
        i = 0
        while n:
            ranged.append(n.pop(-1) if i % 2 == 0 else n.pop(0))
            i +=1
        
        ans = ranged[0]
        for i, v in enumerate(ranged):
            if i == 0:
                continue
            ans = ans - v if i % 2 != 0 else ans + v
        
        return ans 