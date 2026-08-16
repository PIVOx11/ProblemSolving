class Solution:
    def predictPartyVictory(self, s: str) -> str:
        queueR = deque()
        queueD = deque()

        for i, c in enumerate(s):
            if c == "R":
                queueR.append(i)
            else:
                queueD.append(i)
        l = len(s)
        while queueR and queueD:
            R , D = queueR.popleft(), queueD.popleft()
            if R < D:
                queueR.append(R + l)
            else:
                queueD.append(D + l)

        return "Radiant" if queueR else "Dire"
