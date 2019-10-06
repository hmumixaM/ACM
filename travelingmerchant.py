num = int(input())
price = []
for i in range(num):
    price.append(list(map(int, input().split())))

week = []
for i in price:
    result = [i[0]]
    result.append(i[0] + i[1] * 1)
    result.append(i[0] + i[1] * 2)
    result.append(i[0] + i[1] * 3)
    result.append(i[0] + i[1] * 2)
    result.append(i[0] + i[1] * 1)
    result.append(i[0])
    week.append(result)

for _ in range(int(input())):
    begin, end = list(map(int, input().split()))
    for x in ()