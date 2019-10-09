import math

num = int(input())

for i in range(num):
    w, g, h, r = list(map(int, input().split()))
    max = math.sqrt(w**2 + abs(g-h)**2)

    print("{:.8f} {:.8f}".format(max, min))