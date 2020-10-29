import sys
import re

# Task: In each line swap the first and second letters

for line in sys.stdin:
    line = re.sub(r'\b(\w)(\w)(\w*?)\b', r'\2\1\3', line).rstrip()
    print(line)
