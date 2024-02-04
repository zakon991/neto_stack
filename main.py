class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Стэк пустой"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Стэк пустой"

    def size(self):
        return len(self.items)

def is_balanced(expression):
    stack = Stack()

    brackets_dict = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets_dict.values():
            stack.push(char)
        elif char in brackets_dict.keys():
            if stack.is_empty() or stack.pop() != brackets_dict[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


print(is_balanced("(((([{}]))))"))
print(is_balanced("[([])((([[[]]])))]{()}"))
print(is_balanced("{{[()]}}"))
print(is_balanced("}{}"))
print(is_balanced("{{[(])]}}"))
print(is_balanced("[[{())}]"))
