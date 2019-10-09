num = int(input())

last = 1
temp = 0
for i in range(num):
    a = int(input())
    for j in range(last, a):
        print(j)
        temp = 1
    last = a + 1

if temp == 0:
    print("good job")