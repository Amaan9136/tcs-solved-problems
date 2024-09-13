# deque used to obtain double ended queue
from collections import deque

def find_when_friend_served(n, priorities, k):
    queue = deque([(priorities[i], i) for i in range(n)])
    served_count = 0 
    while queue:
        max_priority = max(queue, key=lambda x: x[0])[0]
        current_order = queue.popleft()
        if current_order[0] == max_priority:
            served_count += 1
            if current_order[1] == k:
                return served_count
        else:
            queue.append(current_order)

# Input 
n = int(input().strip()) 
priorities = list(map(int, input().split())) 
k = int(input().strip()) 

# Output 
print(find_when_friend_served(n, priorities, k))
