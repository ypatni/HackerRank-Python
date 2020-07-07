s = set(list(map(int, input().split())))

x = int(input())
arr = []
for i in range(x):
    s3 = set(list(map(int, input().split())))

    check = s.issuperset(s3)
    arr.append(check)

print(all(arr))
    