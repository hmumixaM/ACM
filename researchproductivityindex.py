num = int(input())
listt = list(map(lambda a: int(a)/100, input().split()))
listt.sort()

expect = []
for i in range(num):
    scope = listt[:i+1]
    for j in range(len(scope) - 1):
