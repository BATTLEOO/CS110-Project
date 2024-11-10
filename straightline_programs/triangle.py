import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# ture to standard output if one side <= sum of other
expression =  x <= (y + z) and y <= (x + z) and z <= (y + x)
stdio.writeln(expression)
