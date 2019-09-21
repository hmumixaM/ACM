listt = list(map(int, input().split()))
if listt[0] == 0:
	listt[0] += 24
time = 60 + listt[1] - 45
if time >= 60:
	listt[1] = time - 60
else:
	listt[0] -= 1
	listt[1] = time
print(listt[0], listt[1])
