class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = len(nums)
        if k == l:
            return l

        i = 0
        res = 0
        r = i
        target = k
        while i < l:
            save = i

            while r < l:
                if not target:
                    break
                if nums[r] == 0:
                    target -= 1

                r += 1
            while r < l and nums[r] == 1:
                r += 1

            res = max(res, r - i)
            i += 1
            if nums[i - 1] == 0:
                target += 1

        return res
