A = int(input())
B = int(input())
C = int(input())

result = A * B * C 
num = len(str(result)) -1

data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(str(result))):
    a = (result // (10 ** num))
    result = result - a * 10 ** num
    num -= 1

    for i in range(10):
       if i == a : data[i] += 1


for i in data :
    print(i)



# 백준 다른 문제 정답..ㅎㅎ.. 이렇게 간단히 가능하구나..

a = int(input())
b = int(input())
c = int(input())

d = list(map(int, (str(a * b * c))))

for i in range(10):
    print(d.count(i))