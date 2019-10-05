def truth_to_num(truth):
    if "T" == truth:
        return 1
    else:
        return 0

num = int(input())
values = list(map(truth_to_num, input().split()))
equation = input().split()
equation.reverse()
ind1 = 0

#print(equation)

def lops(number):
    global equation
    global ind1
    if number == 1:
        first = equation[ind1]
        #print(ind1, first)
        ind1 += 1
        if "+" == first:
            val1, val2 = lops(2)
            #print(val1, val2, "Hello +")
            return val1 or val2
        elif "*" == first:
            val1, val2 = lops(2)
            #print(val1, val2, "Hello *")
            return val1 and val2
        elif "-" == first:
            val = lops(1)
            #print(val, "Hello -")
            if not val:
                #print("out 1")
                return 1
            else:
                return 0
        else:
            #print(values[ord(first) - 65])
            return values[ord(first) - 65]
    elif number == 2:
        val1 = lops(1)
        val2 = lops(1)
        return val1, val2

ans = lops(1)
if ans == 1:
    print("T")
else:
    print("F")