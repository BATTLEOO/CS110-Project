import stdio

# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        # instance variables
        # set self._pixels to 0 (int)
        self._pixels = 0

        # set self._x to 0.0 (float)
        self._x = 0.0

        # set self._y to 0.0 (float)
        self._y = 0.0

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):

        # First increment pixels by 1, avoid divide by zero
        self._pixels += 1

        # always remember to put () here if not the result will be wrong
        # the running average is not the simple one, the running average should be the cumulative  running average, this part is the main idea of this method
        # use the running average formular to update the mass of center
        self._x = (self._x * (self._pixels - 1) + x) / self._pixels
        self._y = (self._y * (self._pixels - 1) + y) / self._pixels

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        # return the number of pixels
        return self._pixels

    # Returns the Euclidean distance between the center of mass of this blob and the center of
    # mass of the other blob.
    def distanceTo(self, other):
        # write Euclidean distance formular in the return statement
        # Return the Euclidean distance between the center of mass of self and the center of mass of other
        return ((other._x - self._x)**2 + (other._y - self._y)**2)** 0.5

    # DO NOT EDIT
    # Returns a string representation of this blob.
    def __str__(self):
        return "%d (%.4f, %.4f)" % (self._pixels, self._x, self._y)


# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln("a          = " + str(a))
    stdio.writeln("b          = " + str(b))
    stdio.writeln("dist(a, b) = " + str(a.distanceTo(b)))


if __name__ == "__main__":
    _main()
