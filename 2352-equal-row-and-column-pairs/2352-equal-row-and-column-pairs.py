class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        t = [[0] * len(grid) for r in grid]

        for i in range(len(grid)):
            for j in range(len(grid)):
                t[i][j] = grid[j][i]
        ans = 0

        for r1 in t:
            for r2 in grid:
                if r1 == r2:
                    ans += 1
        return ans
