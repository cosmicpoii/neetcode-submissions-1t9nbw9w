import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add, "-": operator.sub,
                    "*": operator.mul, "/": lambda a, b: int(a / b)}
        
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operators[i](a, b)
                stack.append(result)
        return stack.pop()