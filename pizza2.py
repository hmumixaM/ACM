import math

listt = list(map(int, input().split()))
a = (math.pi * (listt[0] - listt[1])**2 / (math.pi * listt[0]**2) * 100)
print("{:6f}".format(a))