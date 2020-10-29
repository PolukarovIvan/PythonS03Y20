import sys
import re

# Task: In each line replace the first occurrence containing only letter 'a'(ignoring case) with word "argh"

for line in sys.stdin:
    line = re.sub(r'\ba+\b', "argh", line, count=1, flags=re.IGNORECASE)
    print(line)