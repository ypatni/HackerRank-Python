x = int(input())
set1 = set(list(map(int, input().split())))
r = int(input())
for i in range(r):
    command = input().split()
    set2 = set(list(map(int, input().split())))
    if command[0] == "intersection_update":
        set1.intersection_update(set2)
    elif command[0] == "symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    elif command[0] == "difference_update":
        set1.difference_update(set2)
    elif command[0] == "update":
        set1.update(set2)

sum = 0
for i in set1:
    sum+=i
print(sum)