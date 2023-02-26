def reverse_stack(stack):
    new_stack = []
    while stack:
        new_stack.append(stack.pop())
    return new_stack

# Example usage
stack = [1, 2, 3, 4, 5]
reversed_stack = reverse_stack(stack)
print(reversed_stack)  # Output: [5, 4, 3, 2, 1]
