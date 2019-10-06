import math

num = int(input())

for i in range(num):
    w, g, h, r = list(map(int, input().split()))
    max = math.sqrt(w**2 + abs(g-h))
    min = math.sqrt(w**2 + abs(g-h)) + math.sqrt(w**2 + abs(g-h))