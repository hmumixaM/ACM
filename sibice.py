import math

listt = list(map(int, input().split()))
l = math.sqrt(listt[1]**2 + listt[2]**2)
for i in range(listt[0]):
	if int(input()) <= l:
		print('DA')
	else:
		print('NE')
