class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in "+-*/":
                op1 = st[-1]  # Get the top element of the stack
                st.pop()      # Remove the top element
                op2 = st[-1]  # Get the second-to-top element of the stack
                st.pop()      # Remove the second-to-top element

                if t == "+":
                    op = op2 + op1
                elif t == "-":
                    op = op2 - op1
                elif t == "*":
                    op = op2 * op1
                elif t == "/":
                    op = op2 / op1
                st.append(int(op))
            else:
                st.append(int(t))
        return st[0]


        
