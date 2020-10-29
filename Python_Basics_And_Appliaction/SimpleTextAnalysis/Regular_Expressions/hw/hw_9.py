import sys
import re

# Task: in each line replace all occurrences of the same letters with one

for line in sys.stdin:
    line = re.sub(r'(.)\1+', r'\1', line).rstrip()
    print(line)
