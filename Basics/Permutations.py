from itertools import permutations
word, k = input().split()
for i in permutations(sortd(word),int(k)):
    print("".join(i))