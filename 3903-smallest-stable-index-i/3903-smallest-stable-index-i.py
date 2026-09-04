class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = float("inf")

        for i in range(len(nums)):
            che = max(nums[0:i+1]) - min(nums[i: len(nums)])
            if che <= k and i < ans:
                ans = i
        
        return ans if ans != float("inf") else -1