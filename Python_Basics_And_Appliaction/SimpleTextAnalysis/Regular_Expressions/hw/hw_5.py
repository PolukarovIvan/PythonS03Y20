import sys
import re

# Task: Output strings including worlds with two or more same parts

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\b(\w+)\1\b', line):
        print(line)
