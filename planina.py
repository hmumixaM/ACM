num = int(input())
points = 2
for i in range(num):
	points = 2 * points - 1
	num = num - 1
print(points**2)
