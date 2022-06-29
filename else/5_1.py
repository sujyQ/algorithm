stack = []  # Last In First Out

stack.append(5)     # push 5
stack.append(2)     # push 2
stack.append(3)     # push 3
stack.append(7)     # push 7
stack.pop()         # pop
stack.append(1)     # push 1
stack.append(4)     # push 4
stack.pop()         # pop

print(stack)        # [5, 2, 3, 1]
print(stack[::-1])  # [1, 3, 2, 5]