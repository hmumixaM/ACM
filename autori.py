import sys

for line in sys.stdin:
    line = line.split()
    print(abs(int(line[0])-int(line[1])))
