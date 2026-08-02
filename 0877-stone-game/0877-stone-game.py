class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        alice = 0
        bob = 0

        l = 0
        r = len(p) - 1

        turn = 0
        while l < r:
            if p[l] > p[r]:
                res = p[l]
                l += 1
            else:
                r -= 1
                res = p[r]

            if turn == 0:
                alice += res
                turn = 1
            else:
                bob += res
                turn = 0

            alice += p[l]        
    
        return alice > bob