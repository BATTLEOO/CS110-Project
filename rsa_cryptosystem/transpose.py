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
    m = int(len(a))
    n = int(len(a[0]))
    c = stdarray.create2D(n,m,0.0)
    for i in range(n):
        for j in range(m):
            # Notice that we swapped i and j to transpose correctly
            c[i][j] = a[j][i]
    return c


if __name__ == "__main__":
    main()
