num = int(input())
temp = 0.0
for i in range(num):
	listt = list(map(float, input().split()))
	temp += listt[0] * listt[1]
print(temp)
