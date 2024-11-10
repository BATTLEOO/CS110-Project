import stdio
import sys

# create n as int argument
n = int(sys.argv[1])

# set dragon and nogard equal to F
dragon = "F"
nogard = "F"

# using assignment statement to swap each other -- the idea is the same as swapping variable
# set range in 1 to n, and using for loop to repeat the process -- notice to use n + 1, if n will not include n
for i in range(1,n + 1):

# if n is zero, will not be in the condition, the output will be dragon = F, which is in the outer
# set dragon as a temp value, can be swap -- notice that everytime the dragon update from the previous time, we store the new dragon value in temp
    temp = dragon

# when i = 1 temp = F then output dragon = FLF, nogard = temp(F) + R + nogard(F) = FRF
# when i = 2 temp = FLF then output dragon = temp(FLF) + L + nogard(from the previous)(FRF), nogard = temp(FLF) + R + nogard(FRF) = FLFRFRF
# when i = 3 temp = FLFLFRF, then output dragon = temp(FLFLFRF) + L + nogard(FLFRFRF) = FLFLFRFLFLFRFRF nogard = temp(FLFLFRF) + R + nogard(FLFRFRF)
# set dragon
    dragon = dragon + "L" + nogard

# set nogard -- notice that every time i is updated the nogard is also updated
    nogard = temp + "R" + nogard

# notice that the standard output is not in the for loop. Because when n = 0, the for loop will not print anything, so should write standard output outside
stdio.writeln(dragon)