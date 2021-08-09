import sys

n = int(input())

data = list()
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    data.append(a + b)

index = 0
for i in data :
    index += 1
    print("Case #{0}: {1}".format(index, i))