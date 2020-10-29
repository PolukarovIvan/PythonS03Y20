import sys
import re

# Task: Output strings including symbol '\'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\\', line):
        print(line)
