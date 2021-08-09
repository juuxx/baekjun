import sys

n = int(input())

data = list()
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    data.append(a + b)

for i in data :
    print(i)
