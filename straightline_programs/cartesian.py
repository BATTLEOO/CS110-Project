import math
import stdio
import sys

r = float(sys.argv[1])
o = float(sys.argv[2])

x = r * math.cos(math.radians(o))
y = r * math.sin(math.radians(o))

stdio.writeln(str(x) + " " + str(y))
