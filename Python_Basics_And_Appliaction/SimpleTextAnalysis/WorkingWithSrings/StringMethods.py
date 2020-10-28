print("abc" in "abcba")  # Output: True
print("aba" in "abcba")  # Output: False

# method find
print(str.find.__doc__)  # returns -1 on failure
print("cabcbabc".find("abc"))  # Output: 1 - index of the first occurrence
print("cabcbabc".find("df"))  # Output: -1

# method index
print(str.index.__doc__)  # Raises ValueError when the substring is not found
print("cabcbabc".index("abc"))  # Output 1: index of the first found substring

# method startswith
print(str.startswith.__doc__)  # can also deal with tuple
m = ("The dog", "Cabbage", "The Moon", "The Sausage")
s = "The dog iw walking around the valley"
print(s.startswith(m))  # Output: True

# method endswith
m = ("valley", "garden", "apple")
print(s.endswith(m))  # Output: True

# method count
print(str.count.__doc__)
s = "abababa"
print(s.count("aba"))  # Output: 2 - 2 non overlapping occurrences of substring ABAbABA

# right - left travelling
print(str.rfind.__doc__)
print("abacaba".rfind("aba"))  # Output: 4 - highest index in S where substring is found

# methods lower & upper
s = "The man in black fled across the desert, and the gunslinger follows"
print(s.lower())  # returns new string
print(s.upper())  # returns new string
print(s)

# method replace
s = "1,2,3,4"
print(s.replace(',', " ,"))  # returns new string
print(s.replace(',', " ,", 2))  # Output: 1, 2, 3,4

# method strip
s = "   1 2 3 4    \n"
print(s.rstrip())
print(s.lstrip())
print(s.strip())
s = "__1_2_3_4__"
print(s.strip("_"))