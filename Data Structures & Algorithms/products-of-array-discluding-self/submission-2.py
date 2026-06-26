from operator import mul, floordiv
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_list = []
        for i in range(len(nums)):
            total = 1
            ls = nums.copy()
            ls.pop(i)
            for num in ls:
                total *= num
            final_list.append(total)
        return final_list
