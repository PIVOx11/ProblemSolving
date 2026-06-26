from operator  import add, sub, mul, truediv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+":add,
            "-":sub,
            "*":mul,
            "/":truediv
        }

        result = []
        for i in tokens:
            if i not in op:
                result.append(int(i))
            else:
                result[-2] = int(op[i](result[-2], result[-1]))
                result.pop()
        return int(result[0])