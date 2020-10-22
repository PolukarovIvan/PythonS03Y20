lst = [1, 2, 3, 4, 5, 6]

book = {
    "title": "TheLangoLiners",
    "author": "Stephan King",
    "year": 1990
}

iterator = iter(book)
while True:
    try:
        i = next(iterator)
        print(i)
    except StopIteration:
        break

f = open(
    "C:/Users/vanis/PycharmProjects/PythonS03Y20/Python_Basics_And_Appliaction/Standard_Python_Tools/Modules/Modules"
    "/hw/passwords.txt")

while True:
    try:
        print(next(f))
    except StopIteration:
        break

