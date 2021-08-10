data = list()
for i in range(9):
    data.append(int(input()))

max_value = max(data)

index = 1
for i in data :
    if max_value == i :
        print(index)
    index += 1