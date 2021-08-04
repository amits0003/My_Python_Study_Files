from collections import deque

queue = deque(['Amit',1,'Sumit'])

for i in range(5):
    queue.append('Ram')
index=0
while index <= 1:
    index = index+1
    queue.popleft()


print(queue)
