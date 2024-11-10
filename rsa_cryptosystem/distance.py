import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    n = int(sys.argv[1])
    x, y = [], []
    for i in range(n):
        x += [stdio.readFloat()]
    for i in range(n):
        y += [stdio.readFloat()]
    stdio.writeln(_distance(x, y))


def _distance(x, y):
    # set d to 0.0 as float type
    dis = 0.0

    # set n as the number of elements in x
    n = len(x)

    # create for i in range n(exclude)
    for i in range(n):

        # increment dis everytime calculate the point use (x[i] - y[i]) ** 2
        dis += (x[i] - y[i]) ** 2

    # return the value: total dis with sqrt root function
    return math.sqrt(dis)

if __name__ == "__main__":
    main()
