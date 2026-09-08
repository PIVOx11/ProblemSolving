class Solution:
    def increasingTriplet(self, n: List[int]) -> bool:
        if len(n) <= 2 or len(set(n)) <= 2:
            return False
        
        i = j = float("inf")
        for nb in n:
            if nb <= i:
                i = nb
            elif nb <= j:
                j = nb
            else:
                return True

        return False
