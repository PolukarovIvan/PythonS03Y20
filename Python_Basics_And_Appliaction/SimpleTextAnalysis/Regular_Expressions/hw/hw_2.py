import sys
import re

# Task: Output strings containing 'cat' as a world
ans = []
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\bcat\b", line):
        print(line)

