import re

pattern = r'a[ab]+?a'

string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))

pattern = r'(test|text)*'
string = "testtext"
print(re.match(pattern, string))

pattern = r'((abc)|(test|text)*)'
string = [string, "abc", "test", "texttext", "testtest"]
matches = [re.match(pattern, s) for s in string]
for match in matches:
    print(match, match.groups())