f = open("test.txt")

for line in f:
    print(repr(line.rstrip()))