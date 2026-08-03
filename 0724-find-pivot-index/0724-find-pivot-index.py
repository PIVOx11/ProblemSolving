# class Solution:
#     def pivotIndex(self, n: List[int]) -> int:
#         s = sum(n)
#         l = len(n)
#         arr = [0] * (l + 1)

#         for i in range(l + 1):
#             if i > 0:
#                 arr[i] = arr[i - 1] + n[i - 1]

#         for i in range(l):
#             if ((s - n[i]) / 2) == arr[i]:
#                 return i

#         return -1



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        
        for index, value in enumerate(nums):
            total -= value
            if left == total:
                return index
            left += value
        
        return -1