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
    # x and y is a list, idea is to access the x and y by each of them
    # and caluate need a for loop to loop the length first and then x1 anc x2
    dis = 0.0
    n = len(x)
    for i in range(n):
        dis += (x[i] - y[i]) ** 2
    dis = math.sqrt(dis)
    return dis

if __name__ == "__main__":
    main()
