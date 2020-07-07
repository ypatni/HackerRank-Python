t = int(input())
bool = True

for i in range(t):
    x = int(input())
    set1 = set(list(map(int, input().split())))
    y = int(input())
    set2 = set(list(map(int, input().split())))
    s = set()
    for j in set1:
        for k in set2:
            if j ==k:
                s.add(j)
    if(len(s) == len(set1)):
        print(True)
    else: 
        print(False)
    