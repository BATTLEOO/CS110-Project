import stdarray
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = stdarray.create2D(m, n)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdio.readFloat()
    c = _transpose(a)
    for row in c:
        for v in row:
            stdio.write(str(v) + " ")
        stdio.writeln()


# Returns the transpose of a.
def _transpose(a):
    # set m as the number rows in a
    m = int(len(a))

    # set n as the number of columns in a
    n = int(len(a[0]))

    # create c as a 2d list to store the value
    c = stdarray.create2D(n,m,0.0)

    # create i in range n(exclude) as new rows
    for i in range(n):

        # create j in range m(exclude) as new columns
        for j in range(m):

            # assign the number in a to the list c, row to column , column to row
            c[i][j] = a[j][i]

    # return list c
    return c


if __name__ == "__main__":
    main()
