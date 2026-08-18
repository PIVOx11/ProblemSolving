class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        inCase = 0
        
        for i in nums:
            if abs(i) < abs(ans):
                ans = i
            if i == abs(ans):
                inCase = i
        
        if abs(ans) == inCase:
            return inCase
        
        return ans 