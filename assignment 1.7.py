def is_brackets_closed(code_snippet):
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    for char in code_snippet:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return False
            elif brackets[stack.pop()] != char:
                return False
    return not stack

# Example
code_snippet = "{ int a = (4 + 2 )* 6; }"
if is_brackets_closed(code_snippet):
    print("All brackets are closed properly")
else:
    print("Brackets are not closed properly")
