class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        st = set(nums)

        dv = k
        while True:
            if dv not in st and dv % k == 0:
                return dv
            dv += k
            