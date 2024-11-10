import math
import stdio
import sys

o1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

sino2 = math.sin(math.radians(o1)) *n1 / n2
o2 = math.degrees(math.asin(sino2))

stdio.writeln(o2)
