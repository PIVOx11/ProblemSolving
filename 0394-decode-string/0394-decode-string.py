class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        # for c in s:
        #     if c != "]":
        #         if stack and stack[-1].isdigit() and c.isdigit():
        #             stack[-1] += c
        #         else:
        #             stack.append(c)
        #     else:
        #         sub = ""
        #         rep = 1
                
        #         while stack and stack[-1] != '[':
        #             sub = stack.pop() + sub
        #         stack.pop()
                
        #         if stack and stack[-1].isdigit():
        #             rep = int(stack.pop())
        #         sub = sub * rep
        #         stack.append(sub)

        # return "".join(stack)

        c_str = ""
        c_num = 0

        for c in s:
            if c.isdigit():
                c_num = c_num * 10 + int(c)
            elif c == '[':
                stack.append([c_str, c_num])
                c_str = ""
                c_num = 0
            elif c == ']':
                p_str, p_num  = stack.pop()
                c_str = p_str + c_str * p_num
            else:
                c_str += c            

        return c_str