def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

while True:
	num = int(input())
	if num == 0:
		break
	points = []
	for i in range(num):
		points += list(map(int, input().split())),
	print(area(points))
