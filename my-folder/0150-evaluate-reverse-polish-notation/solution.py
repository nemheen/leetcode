class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        ops = "+-/*"
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            elif len(stack) >= 2:
                one = stack.pop()
                two = stack.pop()
                if tokens[i] == '+':
                    res = two + one
                elif tokens[i] == '-':
                    res = two - one
                elif tokens[i] == '/':
                    # Check for division by zero
                    if one != 0:
                        res = int(two / one)
                    else:
                        return "Error: Division by zero"
                else:
                    res = two * one
                stack.append(res)

        return stack[-1]

