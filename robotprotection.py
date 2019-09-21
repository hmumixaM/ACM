import sys
import math
import time

def dotproduct(v1, v2):
	return sum((a*b) for a, b in zip(v1, v2))

def length(v):
	return math.sqrt(dotproduct(v, v))

def angle(l1, l2):
	if length(l1) * length(l2) == 0:
		return 0
	else:
		return math.acos(dotproduct(l1, l2) / (length(l1) * length(l2)))

def lines(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])

def find_min(listt, place):
	pointer = 0
	val = listt[pointer][0]
	for i in range(len(listt)):
		if val > listt[i][place]:
			val = listt[i][place]
			pointer = i
	return pointer

def find_max_angle(points, last_point, last_two_point):
	new_tracker = 0
	temp = 0
	for i in range(len(points)):
		result = angle(lines(points[i], last_point), lines(last_two_point, last_point))
		if result > temp:
			temp = result
			new_tracker = i
	return points[new_tracker], new_tracker


def area(contour):
	results = 0
	for i in range(1, len(contour)-1):
		sin_angle = angle(lines(contour[0], contour[i]), lines(contour[i+1], contour[i]))
		results += math.sin(sin_angle) * length(lines(contour[0], contour[i])) * length(lines(contour[i+1], contour[i])) * 0.5
	return results


while True:
	num = int(input())
	if num == 0:
		break
	points = []
	for i in range(num):
		points += list(map(int, input().split())),
	pointer = find_min(points, 0)
	t0 = time.time()
	print('received: ', t0)


	tracker1 = 0
	tracker2 = 0
	temp = 0
	for i in range(len(points)):
		for j in range(i+1, len(points)):
			angle_result = angle(lines(points[i], points[pointer]), lines(points[j], points[pointer]))
			if angle_result > temp:
				temp = angle_result
				tracker1 = i
				tracker2 = j
	contour = [points[tracker1], points[pointer], points[tracker2]]
	del points[tracker2], points[pointer]
	print("finished: ", time.time() - t0)

	while True:
		new_point, new_tracker = find_max_angle(points, contour[-1], contour[-2])
		if new_point == contour[0]:
			print("{:.1f}".format(area(contour)))
			print("done: ", time.time() - t0)
			break
		else:
			contour.append(new_point)
			del points[new_tracker]