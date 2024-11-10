import math
import stdio
import sys

# create argument a,b,c in float type
a, b, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

# create expression for discriminant
discriminant = b * b - 4 * a * c

# create if statement
# write when a is zero print value of a must not be zero
if a == 0:

# write in standard output
    stdio.writeln("Value of a must not be 0")

# write discriminant print standard output when is less than zero
elif discriminant < 0:

# write in standard output
    stdio.writeln("Value of discriminant must not be negative")

# if did not go through all if and elif conditions, read the else statement
# using the else statement in order to print the other output
else:

#write two root expression, which is root1 and root 2
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

# write in standard output
    stdio.writeln(str(root1) + " " + str(root2))
