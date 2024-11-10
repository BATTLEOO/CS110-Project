import stdio
import sys

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

G = 6.674 * (10 ** -11)

f = G * m1 * m2 / (r ** 2)

stdio.writeln(f)
