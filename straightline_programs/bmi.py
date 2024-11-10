import stdio
import sys

weight = float(sys.argv[1])
height = float(sys.argv[2])

bmi = weight / (height ** 2)

stdio.writeln(bmi)

