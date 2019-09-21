num = int(input())
temp = 0
for i in range(num):
	a = list(input())
	temp += int(''.join(a[:-1]))**int(''.join(a[-1]))
print(temp)
