n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    size = len(data)-1
    avg = sum(data[-size:])/size
    member = 0
    for i in data[-size:] :
            if i > avg : member += 1
    result = member/size*100
    print('{:.3f}%'.format(result))