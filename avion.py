ans = ''

for _ in range(4):
    a = input()
    if 'FBI' in a:
        ans += str(_+1) + ' '
        
a = input()
if 'FBI' in a:
    ans += str(5)
    
if ans == '':
    print('HE GOT AWAY!')
else:
    print(ans)