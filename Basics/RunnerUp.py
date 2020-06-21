n = int(input())
arr = map(int, input().split())
arr = list(arr)
i = max(arr)
j = -100
for x in arr:
    if x>j and x<i:
            
        j = x

print(j)

y = [[r for r in range(5)] for z in range(10)]
print(y)