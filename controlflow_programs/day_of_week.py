import stdio
import sys

# create m d y as int argument
m, d, y = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

# write in expression
y0 = y - (14 - m) // 12
x0 = y0 + y0 // 4 - y0 // 100 + y0 //400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Write condition to all the day such as monday is 1 and so on
# And if the condition touch, write it in standard output
if dow == 0:
    stdio.writeln("Sunday")
elif dow == 1:
    stdio.writeln("Monday")
elif dow == 2:
    stdio.writeln("Tuesday")
elif dow == 3:
    stdio.writeln("Wednesday")
elif dow == 4:
    stdio.writeln("Thursday")
elif dow == 5:
    stdio.writeln("Friday")
elif dow == 6:
    stdio.writeln("Saturday")

# write in standard output if meet the condition
