x = int(input())
arr = list(map(int, input().split()))
s = set(arr)

ans = ((sum(s)*x)-(sum(arr)))//(x-1)
print(ans)