if __name__ == '__main__':
    N = int(input())
    arr = []
    result = []
    for i in range(N):
        sub = input().split()
        arr.append(sub)
    for i in range(len(arr)):
        if arr[i][0] == "insert":
            a = int(arr[i][1])
            b = int(arr[i][2])
            result.insert(a,b)
        elif arr[i][0] == "print":
            print(result)
        elif arr[i][0] == "remove":
            result.remove(int(arr[i][1]))
        elif arr[i][0] == "append":
            result.append(int(arr[i][1]))
        elif arr[i][0] == "sort":
            result.sort()
        elif arr[i][0] == "pop":
            result.pop()
        elif arr[i][0] == "reverse":
            result.reverse()
        
