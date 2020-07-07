x = int(input())
set1 = set(list(map(int, input().split())))
y = int(input())
set2 = set(list(map(int, input().split())))
x = set1.union(set2)
print(len(x))

#intersection()
x = int(input())
set1 = set(list(map(int, input().split())))
y = int(input())
set2 = set(list(map(int, input().split())))
x = set1.intersection(set2)
print(len(x))

#difference
x = int(input())
set1 = set(list(map(int, input().split())))
y = int(input())
set2 = set(list(map(int, input().split())))
x = set1.difference(set2)
print(len(x))

#symmetric_difference

x = int(input())
set1 = set(list(map(int, input().split())))
y = int(input())
set2 = set(list(map(int, input().split())))
x = set1.symmetric_difference(set2)
print(len(x))