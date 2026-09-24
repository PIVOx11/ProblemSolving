class Solution:
    # def smallestIndex(self, nums: List[int]) -> int:
    #     for i, v in enumerate(nums):
    #         v = sum([int(n) for n in str(v)])
    #         if i == v:
    #             return i
        
    #     return -1

    def smallestIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            s = 0
            while v:
                s += v % 10
                v //= 10
            if i == s:
                return i
        
        return -1