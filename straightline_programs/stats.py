import math
import stdio
import stdrandom
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

x1 = stdrandom.uniformFloat(a,b)
x2 = stdrandom.uniformFloat(a,b)
x3 = stdrandom.uniformFloat(a,b)


u = (x1 + x2 + x3) / 3
var = (x1 - u) ** 2 + (x2 - u) ** 2 + (x3 - u) ** 2/ 3
sd = var ** (1 / 2)

stdio.writeln(str(u) + " " + str(var) + " " + str(sd))