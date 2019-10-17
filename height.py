num = int(input())

for _ in range(num):
    listt = list(map(int, input().split()))
    order = listt[0]
    height = listt[1:]
    new = []
    steps = 0
    for i in height:
        count = 0
        for j in new:
            if i < j:
                count += 1
            else:
                break
        new.insert(count, i)
        steps += count
    print(order, steps)