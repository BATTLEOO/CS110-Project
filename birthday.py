import stdarray
import stdio
import stdrandom
import sys

# Set DAYS_PER_YEAR to 365
DAYS_PER_YEAR = 365

# Create trials as int argument
trials = int(sys.argv[1])

# Set count to 0
count = 0

# write for loop in range from 0 to trials, trials do no include
for t in range(0, trials):

# Set birthdaysSeen to a list of size DAYS_PER_YEAR, and make all the value to False
    birthdaysSeen = stdarray.create1D(DAYS_PER_YEAR, False)

# set the while loop to True, make the loop run forever
    while True:

# Increment count by 1, to count the birthday
        count += 1

# Set birthday to a random int from 0 to DAY_PER_YEAR(not include)
        birthday = stdrandom.uniformInt(0, DAYS_PER_YEAR)

# Write an if statement if we the value is true we break
        if birthdaysSeen[birthday]:

# Write the break statement
            break

# If we do not see the birthday before, we move into the else statement assign the True value in the current location
        else:
            birthdaysSeen[birthday] = True

# Write count / trials in standard output, remember we want a floor division, so we use //
stdio.writeln(count//trials)
