import math
import stdio
import sys

avg = float(sys.argv[1])
t = float(sys.argv[2])
p = math.exp(-avg * t)

stdio.writeln(p)
