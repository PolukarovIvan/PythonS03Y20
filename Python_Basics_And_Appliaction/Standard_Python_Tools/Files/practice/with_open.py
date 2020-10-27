with open("test.txt", "r") as f1, \
        open("test1.txt", "r") as f2, \
        open("test2.txt", "r") as f3:
    print("File 1:")
    for line in f1:
        print(line.rstrip(), end=" ")

    print("File 2:")
    for line in f2:
        print(line.rstrip(), end=" ")

    print("File 3:")
    for line in f3:
        print(line.rstrip(), end="")
