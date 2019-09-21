p1 = list(map(lambda x:int(x), input().split()))
p2 = list(map(lambda x:int(x), input().split()))
p3 = list(map(lambda x:int(x), input().split()))
points = (p1, p2, p3)

for i in range(3):
	for j in range(i+1, 3):
		if points[i][0] == points[j][0]:
			points[i][0] = points[j][0] = 0
		if points[i][1] == points[j][1]:
			points[i][1] = points[j][1] = 0
temp = [0, 0]
for i in points:
	if i[0] != 0:
		temp[0] = i[0]
	elif i[1] != 0:
		temp[1] = i[1]
print(temp[0], temp[1])
