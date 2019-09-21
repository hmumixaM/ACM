data = int(input())
months = int(input())
used = 0
for i in range(months):
	used += int(input())
print(data*(months+1)-used)
