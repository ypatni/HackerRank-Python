n = int(input())
s = set(map(int, input().split()))
x = int(input())
for i in range(x):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "discard":
        s.discard(int(command[1]))
    elif command[0] == "remove":
        s.remove(int(command[1]))

sum = 0
for i in s:
    sum = sum + int(i)
print(sum)
