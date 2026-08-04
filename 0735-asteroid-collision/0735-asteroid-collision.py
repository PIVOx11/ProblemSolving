class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = [arr[0]]
        arr.pop(0)
        for ast in arr:
            while stack and stack[-1] > 0 and ast < 0:
                co = stack[-1]
                
                if abs(ast) == abs(co):
                    stack.pop()
                    break
                
                if abs(ast) > abs(co):
                    stack.pop()
                elif abs(ast) < abs(co):
                    break
            else:
                stack.append(ast)

        return stack