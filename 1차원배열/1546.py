n = int(input())

points = list(map(int, input().split()))

max_point = max(points)

new_points = list()
for i in points :
    new_points.append(i/max_point*100)

a = sum(new_points, 0.00)/len(new_points)
print(a)