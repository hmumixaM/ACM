import sys

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.") * 2
dict = {}

for i in sys.stdin:
	if i == "0\n":
		break
	else:
		shift, vocab = i.split()
		for i in range(28):
			dict[alpha[i]] = alpha[i+int(shift)]
		temp = ""
		for j in vocab:
			temp = temp + dict[j]
		word = list(range(len(temp)))
		print(word)
		#print("".join(word))
