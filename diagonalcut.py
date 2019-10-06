import math

num1, num2 = list(map(int, input().split()))


gcd = math.gcd(num1, num2)
a = num1 // gcd
b = num2 // gcd

if a % 2 == 0 or b % 2 == 0:
    count = 0
else:
    count = 1

ans = count * gcd

print(ans)