class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            x = target - numbers[i]
            if x in numbers and i != x:
                return sorted([i + 1, numbers.index(x) + 1])
            i += 1