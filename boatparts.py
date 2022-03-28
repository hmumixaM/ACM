listt = list(map(int, input().split()))

item = []
for i in range(listt[1]):
	stuff = input()
	if stuff in item:
		continue
	else:
		item.append(stuff)
	if len(item) == listt[0]:
		print(i+1)
if len(item) < listt[0]:
	print('paradox avoided')
