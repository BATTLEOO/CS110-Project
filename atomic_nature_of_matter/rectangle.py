import stdio
from interval import Interval


# A data type to represent a rectangle as two (x and y) intervals.
class Rectangle:
    # Constructs a new rectangle given the x and y intervals.
    def __init__(self, xint, yint):
        # Instance variables
        # x-interval of the rectangle, _xint (Interval) initialize
        self._xint = xint

        # y-interval of the rectangle, _yint (Interval) initialize
        self._yint = yint

    # Returns the area of this rectangle.
    def area(self):
        # find the difference between hi and lo, assign the value in a and b
        a = self._xint.upper() - self._xint.lower()
        b = self._yint.upper() - self._yint.lower()

        # and return the area abs(a * b)
        return abs(a * b)

    # Returns the perimeter of this rectangle.
    def perimeter(self):
        # find the difference between hi and lo, assign the value in a and b
        a = self._xint.upper() - self._xint.lower()
        b = self._yint.upper() - self._yint.lower()

        # p is equal to 2 * (abs(a)+ abs(b))
        p = 2 * (abs(a) + abs(b))

        # return the perimeter p
        return p

    # Returns True if this rectangle contains the point (x, y), and False otherwise.
    def contains(self, x, y):
        return self._xint.contains(x) and self._yint.contains(y)

    # Returns True if this rectangle intersects other, and False otherwise.
    def intersects(self, other):
        return self._xint.intersects(other._xint) or self._yint.intersects(other._yint)

    # Returns a string representation of this rectangle.
    def __str__(self):
        return str(self._xint) + " x " + str(self._yint)


# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Rectangle(Interval(-1, 1), Interval(-1, 1))
    b = Rectangle(Interval(0, 2), Interval(0, 3))
    stdio.writeln("a                = " + str(a))
    stdio.writeln("b                = " + str(b))
    stdio.writeln("area(a)          = " + str(a.area()))
    stdio.writeln("perimeter(b)     = " + str(b.perimeter()))
    stdio.writeln("a.contains(1, 5) = " + str(a.contains(1, 5)))
    stdio.writeln("a.intersects(b)  = " + str(a.intersects(b)))


if __name__ == "__main__":
    _main()
