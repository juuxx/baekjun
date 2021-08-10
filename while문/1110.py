def sum(n):
    result = 0
    rightNum = 0
    for i in str(n):
        rightNum = int(i)
        if len(str(n)) == 1:
            result = int(n)
        else:
            result += int(i)

    resultStr = str(result)
    _result = int(str(rightNum) + resultStr[-1:])
    return _result


n = int(input())

result = None
cycle = 0
while result != n:
    if cycle == 0:
        result = n
    result = sum(result)
    cycle += 1

print(cycle)



# 백준 답안 중 하나

N = int(input())
n = -1
t = 0
while n != N:
	if n == -1: n = N
	n = (n//10 + n%10)%10 + (n%10)*10
	t += 1
print(t)

# 와 이렇게 풀수도 있구나 내가 부끄럽네 ㅎㅎ..
# n // 10 -> 앞의 자리수
# n % 10 -> 뒤의 자리수
# (n//10 + n%10)%10 -> 둘이 더해서 2자리수 이상일 수 있으므로 다시 % 10 나눠줌 
# n의 오른쪽 자리수 * 10 으로 해서 둘이 더해줌 
