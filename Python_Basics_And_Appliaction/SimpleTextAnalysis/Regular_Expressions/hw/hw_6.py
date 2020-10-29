import sys
import re

#  Task: in each line replace all occurrences of substring 'human' to substr 'computer'

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'human', 'computer', line)
    print(line)