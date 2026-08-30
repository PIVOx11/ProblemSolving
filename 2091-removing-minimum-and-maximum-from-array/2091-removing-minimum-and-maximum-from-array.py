class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l = len(nums)
        # if l == 1:
        #     return 1
        
        minI, maxI = nums.index(min(nums)), nums.index(max(nums))
        if minI > maxI:
            minI, maxI = maxI, minI
        
        left = maxI + 1
        right = l - minI
        
        both =  (minI + 1) + (l - (maxI))

        print(left, right, both)

        return min(left, right, both)