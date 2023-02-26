def prefix_to_infix(expression):
    stack = []

    for i in range(len(expression)-1, -1, -1):
        char = expression[i]
        if char.isalpha() or char.isdigit():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")

    return stack[-1]

# Example
prefix_expression = "+AB"
infix_expression = prefix_to_infix(prefix_expression)
print(infix_expression) 
