import math

def dotproduct(v1, v2):
    return sum((a * b) for a, b in zip(v1, v2))

def crossproduct(a, b):
	return a[0] * b[1] - a[1] * b[0]

def length(v):
    return math.sqrt(dotproduct(v, v))

def lines(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def cos_angle(l1, l2):
	if length(l1) == 0 or length(l2) == 0:
		return 0
	else:
		return 1 - dotproduct(l1, l2) / (length(l1) * length(l2))

def area(set):
	area = 0
	for i in range(len(set)-1):
		area += set[i][0] * set[i+1][1] - set[i][1] * set[i+1][0]
	area += set[-1][0] * set[0][1] - set[-1][1] * set[0][0]
	area /= 2
	return abs(area)

while True:
	num = int(input())
	if num == 0:
		break
	points = []
	for i in range(num):
		points += list(map(int, input().split())),
	min_point = min(points, key=lambda angle: angle[1])
	points.remove(min_point)

	angles = [(0, min_point),]
	for point in points:
		angles.append((cos_angle(lines(point, min_point), (1,0)), point))
	angles.sort(key = lambda angle: angle[0])
	angles.append((0,min_point))

	contour = [angles[0][1]]
	k = 0
	while True:
		if k+2 >= len(angles):
			break
		l1 = lines(angles[k+1][1], contour[-1])
		l2 = lines(angles[k+2][1], angles[k+1][1])
		a = crossproduct(l1, l2)
		if crossproduct(l1, l2) <= 0:
			angles.remove(angles[k+1])
			k -= 1
			if angles[k+1][1] in contour:
				contour.remove(angles[k+1][1])
			continue
		else:
			contour.append(angles[k+1][1])
			k += 1


	print("{:.1f}".format(area(contour)))