from itertools import permutations
word, k = input().split()
for i in permutations(sorted(word),int(k)):
    print("".join(i))