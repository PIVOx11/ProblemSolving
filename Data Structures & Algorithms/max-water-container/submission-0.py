class Solution:
    def maxArea(self, h: List[int]) -> int:
        x, y = 0, len(h) - 1
        result = 0
        while x < y:
            if h[x] <= h[y]:
                check = (y - x) * h[x]
            else:
                check = (y - x) * h[y]
            if check > result:
                result = check
            if h[x] >= h[y]:
                y -= 1
            else:
                x += 1
        return result