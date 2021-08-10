#1
while True :
    try:
        a, b = map(int, input().split())
        print(a + b)
    except :
        break

#2-1
import sys

lines = sys.stdin.readlines()
for line in lines :
    a, b = map(int, line.split())
    print

#2-2
for line in sys.stdin :
    a, b = map(int, line.split())
    print(a+b)
