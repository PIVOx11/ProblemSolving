class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        result = []
        nums.sort()

        print(nums)
        for i, a in enumerate(nums):
            
            if i > 0 and a == nums[i - 1]:
                continue
            b = i + 1
            c = len(nums) - 1
            while b < c:
                check = a + nums[b] + nums[c]
                if check > 0:
                    c -= 1
                elif check < 0:
                    b += 1
                else:
                    result.append([a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
        return result