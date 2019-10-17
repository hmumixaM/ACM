n, p, k = list(map(int, input().split()))
time = list(map(int, input().split()))
last = 0
total = 0
mark = 0
p = p / 100
time.append(k)
for i in time:
    total += (i - last) * (1 + mark * p)
    mark += 1
    last = i
print(total)