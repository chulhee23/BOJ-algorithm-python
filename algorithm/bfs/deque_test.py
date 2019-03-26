from collections import deque
queue = deque()
queue.append(1)
queue.append(2)

queue.appendleft(3)
queue.appendleft(4)

print(queue)

queue.pop()
queue.popleft()

print(queue)
