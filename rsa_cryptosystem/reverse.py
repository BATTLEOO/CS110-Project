import stdio


# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a:
        stdio.writef("%s ", v)
    stdio.writeln()


# Reverses a in place, ie, without creating a new list.
def _reverse(a):

    # set n to len(a) for easy to use
    n = len(a)

    # create a for loop in half of the len(a), we do not need go though all of len(a)
    for i in range(n//2):

        # we swap value between two side of the number, the most right and the most
        # most right, use i to narrow the range
        temp = a[i]
        a[i] = a[n -1 - i]
        a[n - 1 - i] = temp

    # we return a to _reverse(a)
    return a
# remember have to put the return a out of the for loop
# if put return a  in the for loop l and t will not swap each other


if __name__ == "__main__":
    main()
