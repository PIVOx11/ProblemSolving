class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # First Idea
        # n = sorted(list(set(n)))

        # return n[-3] if len(n) >= 3 else max(n)
        
        
        # n = set(n)
        # if len(n) < 3:
        #     return max(n)
        
        # t = max(n)
        # s = f = -float("inf")

        # for n in n:
        #     if n > f:
        #         f, s, t = n, f, s
        #     elif n > s:
        #         s, t = n, s
        #     elif n > t:
        #         t = n
        
        # return t

        # Sort the array.
        nums.sort(reverse = True)
        
        elem_counted = 1
        prev_elem = nums[0]
        
        for index in range(len(nums)):
            # Current element is different from previous.
            if nums[index] != prev_elem:
                elem_counted += 1
                prev_elem = nums[index]
            
            # If we have counted 3 numbers then return current number.
            if elem_counted == 3:
                return nums[index]
        
        # We never counted 3 distinct numbers, return largest number.
        return nums[0]

