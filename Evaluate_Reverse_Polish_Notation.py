class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    if op1*op2 < 0 and op1 % op2  != 0:
                        stack.append(op1 // op2 + 1)
                    else:
                        stack.append(op1 // op2)
            return stack[0]