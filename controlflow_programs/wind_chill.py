import stdio
import sys

# Create t and v as float arguments
t, v = float(sys.argv[1]), float(sys.argv[2])

# Create the expression for the wind chill (w)
w = 35.74 +0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)

# write if statement
# write t is bigger than 50 as condition
if t > 50:

# write in standard output
    stdio.writeln("Value of t must be <= 50 F")

# write v is less than equal to 3 as a condition
elif v <=3:

# write in standard output
    stdio.writeln("Value of v must be > 3 mph")

# if did not pass all the conditions write w in standard output
else:

# write w in standard output
    stdio.writeln(w)

