class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_track = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in map_track:
                if stack and map_track[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False