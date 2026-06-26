class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        i, j = 0, len(n) - 1
        while i < j:
            check = n[i] + n[j]
            if check > target:
                j -= 1
            elif check < target:
                i += 1
            else:
                return [i + 1, j + 1]