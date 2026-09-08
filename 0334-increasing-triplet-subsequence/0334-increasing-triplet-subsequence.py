class Solution:
    def increasingTriplet(self, n: List[int]) -> bool:
        if len(n) <= 2 or len(set(n)) <= 2:
            return False
        
        l = len(n)
        i = 0
        j = 1
        k = 2

        while k < l and j < l and i < l:
            if n[i] < n[j] < n[k]:
                return True
            
            if n[i] >= n[j]:
                i += 1
                if j == i:
                    j += 1
                    if j == k:
                        k += 1
            elif n[k] <= n[j]:
                k += 1
            
            if k == len(n):
                j += 1
                k = j + 1
            
        return False
