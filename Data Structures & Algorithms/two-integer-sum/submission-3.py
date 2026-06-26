class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for x in nums:
            check = target - x
            if str(check) in map:
                print(check)
                return [map[str(check)], nums.index(x)]
            if check in nums:
                map[str(x)] = nums.index(x)
                nums[nums.index(x)] = "_"