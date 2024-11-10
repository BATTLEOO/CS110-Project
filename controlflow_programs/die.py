import stdio
import stdrandom

# Set value to a random integer from 1 to 6.
value = stdrandom.uniformInt(1, 7)

# Set output to the empty string. because we need output to print the value
# so decide to use a empty string as initialize
output = ""

# Set output to the appropriate string based on value.
# create if statement and write all the condition
if value == 1:
    output = '     \n  *  \n     '
elif value == 2:
    output = '*    \n     \n    *'
elif value == 3:
    output = '*    \n  *  \n    *'
elif value == 4:
    output = '*   *\n     \n*   *'
elif value == 5:
    output = '*   *\n  *  \n*   *'
elif value == 6:
    output = '*   *\n*   *\n*   *'


# Write output to standard output.
stdio.writeln(str(output))
