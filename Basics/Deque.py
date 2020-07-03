from collections import deque 
 
x = int(input())
d = deque()
for i in range(x):
    command = input().split()
    
    if(command[0] == "append"):
        d.append(int(command[1]))
    elif(command[0] == "appendleft" ):
        d.appendleft(int(command[1]))
    elif(command[0] == "pop"):
        d.pop()
    elif(command[0] == "popleft"):
        d.popleft()
for i in d:
    print(i,end = ' ')
