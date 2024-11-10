import stdio
import sys

input1 = int(sys.argv[1])
input2 = int(sys.argv[2])
input3 = int(sys.argv[3])


largest = max(input1, input2, input3)
smallest = min(input1, input2, input3)
mid = (input1 + input2 + input3) - largest - smallest

stdio.writeln(str(smallest) + " " + str(mid) + " " + str(largest))
