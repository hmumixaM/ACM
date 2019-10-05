events = list(input())
alpha = []
for _ in range(26):
    alpha.append(0)

for i in events:
    alpha[ord(i) - 97] += 1

count = []
for i in alpha:
    if i > 0:
        count.append(i)

perm1 = len(events) - 2
result = math.factorial(perm1)
for i in count:
    result = result / i

result = comb * result
print(result)