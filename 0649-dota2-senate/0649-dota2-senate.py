class Solution:
    def predictPartyVictory(self, s: str) -> str:
        queueR = deque()
        queueD = deque()

        for i, c in enumerate(s):
            if c == "R":
                queueR.append(i)
            else:
                queueD.append(i)
        
        while queueR and queueD:
            R , D = queueR.popleft(), queueD.popleft()
            if R < D:
                queueR.append(R + len(s))
            else:
                queueD.append(D + len(s))

        return "Radiant" if not queueD else "Dire"
