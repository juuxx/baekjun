n = int(input())
for i in range(n):
    a = list(input())
    
    result = 0 
    before = 0
    for j in a :
        if j == 'O':
            before += 1
            result += before
        if j == 'X':
            before = 0
            result += before
    
    print(result)

