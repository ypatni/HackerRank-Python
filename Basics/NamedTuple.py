from collections import namedtuple

n = int(input())
attr = input().split()
marks = []
Student = namedtuple('Student', attr)
for i in range(n):
    marks.append(int(Student._make(input().split()).MARKS))
print("{:.2f}".format((sum(marks) / len(marks))))