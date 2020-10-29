import re

# . ^ $ * + ? {} [] \ |  () - meta symbols
# [] -- you may specify set of appropriate characters

pattern1 = r'a[a-d]c'  # includes all symbols from a to d
pattern2 = r'a[a-zA-Z]c'  # includes all upper and lower case symbols
pattern3 = r'a[^a-zA-z]c'  # not includes all letters

# \d ~ [0-9]- all digits
# \D ~ [^0-9] - everything but digits
# \s ~ [\t\n\r\f\v] - extra symbols
# \S ~ [^\t\n\r\f\v] - everything but extra symbols
# \w ~ [a-zA-Z0-9_] - lower and upper case letters, digits and "_"
# \W ~ [^a-zA-Z0-9_] - in addition to all of the above

pattern = r'a[\w]c'
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)

string = 'abc, a.c, aac, a-c, aBc, azc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)

pattern = r'a.c'  # - all symbols
fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)

# repeating
pattern1 = r'ab*a'  # ~ aa | aba | abba ...
pattern2 = r'ab+a'  # ~ aba, abba, abbba ...
pattern3 = r'ab?a'  # aa, aba - 0 or 1 occurrence
pattern4 = r'ab{2,6}a'  # from 2 to 6 letters 'b' between

all_inclusions1 = re.findall(pattern1, "abba, aa, ab, abbbbbba")
all_inclusions2 = re.findall(pattern2, "abba, aa, ab, abbbbbba")
print(all_inclusions1, all_inclusions2)

pattern = r'a.*a'  # - all symbols
all_inclusions2 = re.findall(pattern, "abba, aa, ab, abbbbbba, aba")
print(all_inclusions2)