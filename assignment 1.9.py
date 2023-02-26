class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, item):
        self.items.append(item)
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)

    def pop(self):
        if not self.items:
            return None
        item = self.items.pop()
        if item == self.min_items[-1]:
            self.min_items.pop()
        return item

    def get_min(self):
        if not self.min_items:
            return None
        return self.min_items[-1]


stack = Stack()

stack.push(4)
stack.push(3)
stack.push(5)
stack.push(1)

print("The smallest number in the stack is:", stack.get_min())
