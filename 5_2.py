from collections import deque

queue = deque()         # First In First Out

queue.append(5)         # push 5
queue.append(2)         # push 2
queue.append(3)         # push 3
queue.append(7)         # push 7
queue.popleft()             # pop
queue.append(1)         # push 1
queue.append(4)         # push 4
queue.popleft()             # pop

print(queue)            # deque([3, 7, 1, 4])
queue.reverse()
print(queue)            # deque([4, 1, 7, 3])

print(list(queue))      # [4, 1, 7, 3]