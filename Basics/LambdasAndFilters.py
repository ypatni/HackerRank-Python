seq = list(range(0,21))
t = list(filter(lambda x: x%2 == 0,seq))
for i in range(len(t)) :
    print(t[i], end = " ")