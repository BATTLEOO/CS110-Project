import stdio
import stdaudio
import sys

# readAllInts is already a list, store our input in measures

measures  = stdio.readAllInts()

# write an if statement if the input is no equal to 32 -- also use len(measures) to check the number of input
# if not equal to 32, print the message by using sys.exit()
if len(measures) != 32:

# write the message if not equal to 32
    sys.exit(str("A waltz must contain exactly 32 measures"))

# write for i in range from measures[0] to measures[15], because we want to check the first 16 value is from minuet measure
for i in range(16):

# write if is not between 1 and 176
    if 1 > measures[i] > 176:

# if not , we print a status say it must between 1 and 176
        sys.exit(str("A minuet measure must be from [1, 176]"))

# write for loop i in range form 16 to 32 the last 16 elements that we want to access
for i in range(16, 32):

# we use if statement to check is the value between 1 and 96
    if 1 > measures[i] > 96:

# if not between, we print a status say it must between 1 and 96
        sys.exit(str("A trio measure must be from [1, 96]"))


# set a for loop v in range from [0] to [15], we want at to have the first 16 value
for v in range(16):

# we store the value in waltz each time
    minuet = measures[v]

# we set the file name
    filename = 'data/M' + str(minuet)

# we use stdaudio.playFile to play the music which choose from M.wav
    stdaudio.playFile(filename)


# set a for loop v in range from [16] to [31], we want at to have the last 16 value
for v in range(16, 32):

 # we store the value in trio each time
    trio = measures[v]

# we set the file name
    filename = 'data/T' + str(trio)

# we use stdaudio.playFile to play the music which choose from T.wav
    stdaudio.playFile(filename)


# PROBLEM:
# !! WINDOWS CANNOT PLAY THE MUSIC DUE TO ITS CAPABILITY
# The problem happen at line 45, and might also happen at line 55, error type is run time error
# TESTING IN PYGAME, success to play the file, but when use stdaudio.playFile, not able to play the file.

# PROBLEM SOLUTION -- 2024/10/21
# IMPORT THE LATEST STDADUIO LIBRARY , THEN THE CODE IS ABLE TO RUN

# FOR RUNNING THE CODE : python generatewaltz.py < data/mozart.txt | python playwaltz.py
