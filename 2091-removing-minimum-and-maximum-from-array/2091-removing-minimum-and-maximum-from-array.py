class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l = len(nums)
        
        minI, maxI = nums.index(min(nums)), nums.index(max(nums))
        if minI == maxI: return 1
        if minI > maxI:
            minI, maxI = maxI, minI
        
        left = maxI + 1
        right = l - minI
        
        both =  (minI + 1) + (l - (maxI))

        print(left, right, both)

        return min(left, right, both)