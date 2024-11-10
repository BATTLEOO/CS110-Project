import stdio
import sys

# Accept n as command-line argument
n = int(sys.argv[1])

# set a equal to 1
a = 1

# write while loop, repeat as long as a^3 ≤ n
while (a * a * a) <= n:

# Set b (int) to a +1
    b = a + 1

# write while loop, repeat as long as a^3 +b^3 ≤ n
    while (b * b * b) + (a * a * a)<= n:

# Set c (int) to a +1
        c = a + 1

# write while loop, repeat as long as c^3 ≤ n
        while (c * c * c) <= n:

# Set d (int) to c +1
            d = c + 1

# write while loop, repeat as long as c^3 +d^3 ≤ n
            while (d * d * d) + (c * c * c) <= n:

#  Set x (int) to a^3 +b^3 and y (int) to c^3 +d^3
                x = (a * a * a) + (b * b * b)
                y = (c * c * c) + (d * d * d)

# If x = y, write “x = aˆ3+bˆ3 = cˆ3+dˆ3 if meet the condition, write in standard output
                if x == y:
                    stdio.writeln(str(x) + ' = ' + str(a) + '^3 + ' + str(b) + '^3 = ' + str(c) + '^3 + ' + str(d) + '^3')

# Increment d by 1
                d += 1

# Increment c by 1
            c += 1

# Increment b by 1
        b += 1

# Increment a by 1
    a += 1
