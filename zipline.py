import math

num = int(input())

for i in range(num):
    w, g, h, r = list(map(int, input().split()))
    min = math.sqrt(w**2 + abs(g-h)**2)
    if 2 * r == g + h:
        d = w / 2
    else:
        d = (g - r) * w / (g + h - 2 * r)
    max = math.sqrt(d**2 + abs(g-r)**2) + math.sqrt((w-d)**2 + abs(h-r)**2)
    print("{:.8f} {:.8f}".format(min, max))