class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0
        target = [{2, 3, 4, 5}, {4, 5, 6, 7}, {6, 7, 8, 9}]
        seatMap = defaultdict(set)

        for r in reservedSeats:
            row , seat = r
            seatMap[row].add(seat)

        for reSeats in seatMap.values():
            first = not (target[0] & reSeats) 
            mid = not (target[1] & reSeats)
            last = not (target[2] & reSeats)
            
            if first and last:
                ans += 2
            elif first or last or mid:
                ans += 1

        return ans + (n - len(seatMap)) * 2
                    
