import sys

n = int(input())

data = list()
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))

# index = 0
# for i in data :
#     index += 1
#     print("Case #{0}: {1} + {2} = {3}".format(index, i[0], i[1], i[0] + i[1]))

#굳이 input이랑 출력 부분이랑 나눌 필요 없었음.


