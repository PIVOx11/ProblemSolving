class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        arrMap = {}
        ans = []

        for i in nums:
            if i not in arrMap:
                arrMap[i] = arr.index(i)
            ans.append(arrMap[i])
        return ans