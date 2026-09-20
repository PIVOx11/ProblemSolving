class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        n = sorted(list(set(nums)))

        return n[-3] if len(n) >= 3 else max(n)