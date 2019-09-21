key = "".join(input().split()).upper()
text = list("".join(input().split()).upper())
alphabet = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")

table = []
for i in list(key)+alphabet:
	if not i in table:
		table.append(i)

dict = {}
for i in range(len(table)):
	dict[table[i]] = i

index = 0
temp = ""
while(index < len(text)):
	if index == (len(text)-1):
		text.append("X")
	if text[index] == text[index+1]:
		text.insert(index+1, "X")
	val1 = dict[text[index]]
	val2 = dict[text[index+1]]
	if val1//5 == val2//5:
		temp += str(table[(val1%5+1)%5+val1-val1%5]) + str(table[(val2%5+1)%5+val2-val2%5])
	elif val1%5 == val2%5:
                temp += str(table[(val1+5)%25]) + str(table[(val2+5)%25])
	else:
		temp += str(table[val1//5*5+val2%5]) + str(table[val1%5+val2//5*5]
)
	index += 2

print(temp)
