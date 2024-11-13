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

    # set n as the number of elements in a (the length of a)
    n = len(a)

    # create a for loop in range from 0 to the n//2 (exclude)
    for i in range(n//2):

        # swapping value : a[i] and a[n - i - 1] , and use temp to store a[i]
        temp = a[i]
        a[i] = a[n -1 - i]
        a[n - 1 - i] = temp

    # return a to _reverse(a)
    return a

if __name__ == "__main__":
    main()
