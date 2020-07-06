# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for i in range(t):
    try: 
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)
