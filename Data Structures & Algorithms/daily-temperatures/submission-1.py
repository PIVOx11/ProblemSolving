class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        result = []
        for i, v in enumerate(t):
            j = i
            while j < len(t) - 1 and v >= t[j]:
                j += 1
            result.append(j - i) if t[j] > v else result.append(0)
            
        return result