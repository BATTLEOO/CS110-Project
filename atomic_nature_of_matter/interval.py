import stdio


# A data type to represent a 1-dimensional interval [lbound, ubound].
class Interval:
    # Construct a new interval given its lower and upper bounds.
    def __init__(self, lbound, ubound):
        self._lbound = lbound
        self._ubound = ubound

    # Returns the lower bound of this interval.
    def lower(self):
        return self._lbound

    # Returns the upper bound of this interval.
    def upper(self):
        return self._ubound

    # Returns True if this interval contains the point x, and False otherwise.
    def contains(self, x):
        if self._ubound >= x >= self._lbound:
            return True
        else:
            return False

    # Returns True if this interval intersects other, and False otherwise.
    def intersects(self, other):

        if self._lbound <= other._ubound and other._lbound <= self._ubound:
            return True
        else:
            return False


    # Returns a string representation of this interval.
    def __str__(self):
        return "[" + str(self._lbound) + ", " + str(self._ubound) + "]"


# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Interval(-2, 1)
    b = Interval(0, 3)
    stdio.writeln("a                     = " + str(a))
    stdio.writeln("b                     = " + str(b))
    stdio.writeln("a.contains(b.lower()) = " + str(a.contains(b.lower())))
    stdio.writeln("a.contains(b.upper()) = " + str(a.contains(b.upper())))
    stdio.writeln("a.intersects(b)       = " + str(a.intersects(b)))

if __name__ == "__main__":
    _main()
