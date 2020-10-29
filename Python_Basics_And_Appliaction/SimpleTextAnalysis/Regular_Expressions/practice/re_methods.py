import re

print(re.findall, re.search, re.sub, re.match, sep='\n')

pattern = r"abc"
string = "babc"

match_object = re.match(pattern, string)  # compares prefix of our string with the pattern
print(match_object)

match_object = re.search(pattern, string)  # finds occurrence of the pattern to the string
print(match_object)

pattern = r"a[abc]c"  # [the set of symbols] ~ aac | abc | acc

print(re.match(pattern, 'aac'))  # Output: re.Match object
print(re.match(pattern, 'abc'))  # Output: re.Match object
print(re.match(pattern, 'acc'))  # Output: re.Match object
print(re.match(pattern, 'aoc'))  # Output: None

string = "abc, acc, abc, abcac, alo nu kak tam s dengami"

all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

fixed_typos = re.sub(pattern, "oooo", string)
print(fixed_typos)

