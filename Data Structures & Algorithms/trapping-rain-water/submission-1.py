class Solution:
    def trap(self, h: List[int]) -> int:
        max_right = []
        max_left = []
        result = 0
        for i in range(len(h)):
            if i == 0:
                max_left.append(0)
                continue
            if i < len(h) and max_left[-1] >= h[i - 1]:
                max_left.append(max_left[-1])
            else:
                max_left.append(h[i - 1])
        
        x = len(h) - 1
        while x >= 0:
            if x == len(h) - 1:
                max_right.append(0)
                x -= 1
                continue
            if h[x + 1] >= max_right[0]:
                max_right.insert(0, h[x + 1])
            else:
                max_right.insert(0, max_right[0])
            x -= 1
        
        for i in range(len(h)):
            mini = min(max_left[i], max_right[i])
            mini -= h[i]
            if mini > 0:
                result += mini
        return result