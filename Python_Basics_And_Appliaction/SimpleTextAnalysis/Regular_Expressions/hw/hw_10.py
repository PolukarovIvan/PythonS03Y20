import sys
import re

expr = r"/^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1(0+)?)|(0(0+)?)))$/"

for line in sys.stdin:
    line = line.rstrip()
    if re.search(expr, line):
        print(line)
