import re
x = int(input())

for i in range(x):
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)