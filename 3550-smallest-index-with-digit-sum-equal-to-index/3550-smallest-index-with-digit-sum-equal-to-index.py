class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            v = sum([int(n) for n in str(v)])
            if i == v:
                return i
        
        return -1