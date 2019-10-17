a = list(input())
b = list(input())
if len(a) >= len(b):
    a.insert(len(a) - len(b) + 1, '.')
    while a[-1] == "0":
        a = a[:-1]
    if a[-1] == '.':
        a = a[:-1]
    print(''.join(a))
elif len(a) <= len(b):
    zero = ''
    for _ in range(len(b) - len(a)):
        zero += '0'
    a.insert(0, zero)
    a = list(''.join(a))
    a.insert(1, '.')
    print(''.join(a))
