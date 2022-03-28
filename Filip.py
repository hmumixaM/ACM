listt = list(map(int, input().split()))
temp = [str(listt[0]), str(listt[1])]
temp = [int(temp[0][2] + temp[0][1] + temp[0][0]), int(temp[1][2] + temp[1][1] + temp[1][0])]

print(max(temp))
