f = open("test1.txt", "w")

f.write("Hello!\n")
f.write("Abraham\n")

lines = ["String 1", "String 2", "String 3"]

f.write("\n".join(lines))

f.close()


