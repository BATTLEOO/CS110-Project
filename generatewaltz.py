import stdarray
import stdrandom
import stdio

#  Create a 2D list called minuetMeasures with dimensions 11 × 16
minuetMeasures = stdarray.create2D(11, 16, 0)

# create a for loop i in range 11 (11 not include) -- we want to read all the value from the txt for minuet
for i in range(11):

# create a for loop j in range 16 (16 not include)
    for j in range(16):

# we read the value form the user input, then we store the value to the 2d list one by one, the first value store in minuetMeasures[0][0]
        minuetMeasures[i][j] = stdio.readInt()

# Create a 2D list called trioMeasures with dimensions 6 × 16
trioMeasures = stdarray.create2D(6, 16, 0)

# create a for loop i in range 6 (6 not include) -- we want to read all the value from the txt for trio
for i in range(6):

# create a for loop j in range 16 (16 not include)
    for j in range(16):

# we read the value form the user input, then we store the value to the 2d list one by one, the first value store in trioMeasures[0][0]
        trioMeasures[i][j] = stdio.readInt()

# create a for loop in range from 0 to 15 + 1, (include 15)
for j in range(0, 16):

# set i to the sum of two die rolls (ram1 and ram2)
# each a random number from 1 to 6 + 1
    ram1 = stdrandom.uniformInt(1, 7)
    ram2 = stdrandom.uniformInt(1, 7)

# set i is equal to the sum of two randon number
    i = ram1 + ram2

# Write minuetMeasures[i − 2][j] with a space after in standard output
    stdio.write(str(minuetMeasures[i-2][j]) + " ")

# create a for loop in range from 0 to 15 + 1, (include 15)
for j in range(0, 16):

# Set i to the value of a die roll (a random number from 1 to 6 + 1)
    i = stdrandom.uniformInt(1, 7)

# Write trioMeasures[i − 1][j] with a space after in standard output
    stdio.write(str(trioMeasures[i - 1][j]) + " ")

# write a newline
stdio.writeln()

