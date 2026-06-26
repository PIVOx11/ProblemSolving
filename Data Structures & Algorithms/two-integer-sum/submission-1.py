class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            check = target - x
            if check in nums:
                try:
                    x1 = nums.index(x)
                    nums[nums.index(x)] = "_"
                    x2 = nums.index(check)
                    return [x1, x2]
                except Exception:
                    continue