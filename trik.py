order = list(input())
ball = [1, 0, 0]
for i in order:
	if i == 'A':
		temp = ball[0]
		ball[0] = ball[1]
		ball[1] = temp
	if i == 'B':
                temp = ball[1]
                ball[1] = ball[2]
                ball[2] = temp
	if i == 'C':
                temp = ball[0]
                ball[0] = ball[2]
                ball[2] = temp
print(ball.index(1)+1)
