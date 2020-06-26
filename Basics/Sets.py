def average(array):
    # your code goes here
        x = set(array)
        a = sum(x)
        return a/len(x)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)