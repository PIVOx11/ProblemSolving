class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        p = nums[0]
        counter = 1
        i = 0
        while i < len(nums):
            if nums[i] != p:
                p = nums[i]
                counter += 1


            if counter == 3:
                return nums[i]

            i += 1
        return nums[0]