class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")

        i = 0
        j = 0
        l = len(nums)
        s = nums[i]
        
        while j < l: 
            if s >= target:
                res = min(res, (j + 1) - i)
                s -= nums[i]
                i += 1
            else:
                j += 1
                if j < l:
                    s += nums[j]
        
        return res if res != float("inf") else 0
        

            

