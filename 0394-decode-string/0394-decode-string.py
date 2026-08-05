class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                if stack and stack[-1].isdigit() and c.isdigit():
                    stack[-1] += c
                else:
                    stack.append(c)
            else:
                sub = ""
                rep = 1
                
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                stack.pop()
                
                if stack and stack[-1].isdigit():
                    rep = int(stack.pop())
                sub = sub * rep
                stack.append(sub)

        return "".join(stack)