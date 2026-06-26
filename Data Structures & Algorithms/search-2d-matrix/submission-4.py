class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target > i[-1]:
                continue
            else:
                if target in i:
                    return True
                return False
        return False