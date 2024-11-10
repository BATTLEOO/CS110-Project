import stdio
import stdrandom
import sys

n = int(sys.argv[1])

r1 = stdrandom.uniformInt(1,n +1)
r2 = stdrandom.uniformInt(1,n +1)

s = r1 + r2

stdio.writeln(s)
