import sys
import re

# Task: Output strings, including 2 letters 'z' and 3 symbols between

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"z.{3}z", line):  # ~ r'z...z'
        print(line)