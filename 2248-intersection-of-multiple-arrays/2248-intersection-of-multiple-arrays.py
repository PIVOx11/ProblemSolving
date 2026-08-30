class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for arr in nums:
            ans = ans & set(arr)

        return sorted(list(ans))