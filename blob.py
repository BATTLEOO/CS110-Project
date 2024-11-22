from pygame.gfxdraw import pixel

import stdio
# CODE HAS BEEN FIXED, DO NOT EDIT UNLESS THERE IS ISSUE IN FURTHER PROGRAM

# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        #CORRECT CODE : DO NOT EDIT
        # leave the self as empty as default
        # initial the pixels as int and x and y as float
        # because it have to be a emtpy constructs because have empty Blob in main()
        # which means that if create parameter, the program will not work without any parameter provided
        # we want to set all the data that not explict need input from the user
        self._pixels = 0
        self._x = 0.0
        self._y = 0.0

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):
        # CODE IS CORRECT: DO NOT EDIT
        # assume i update my x and y every time a new x y is put in side bolb
        # use the idea of running average to update the center of mass(x, y) of blob(particle)
        # add pixels coordinates to blob(particle) and update the center of mass dynamically,
        # so the center of mass is between x and y which is the middle point between x and y , add the pixel in the center of the particle(blob)
        # if the same blob call add pixel to this blob what will happen
            # assume, (1, 1) then we put pixel in the center of mass, now we have the center of mass for 1, 1
            # nexttime, we add (2, 2) a new value of x, y, we put pixel put the pixel in the center of mass in a new center, which is a new one. (for the running average still not sure)
                # the advice is to use the idea of running average, for here is to sum of x and y, and then divde 2 because only two coordinate
            # everytime we add a new pixel, we record we have add one brand new pixel to this blob
        # how to implement dynamically
        # increment pixels by 1, i move it here because pixels can not divide by zero
        self._pixels += 1
        # so the mid point idea is good and it is divide by the number of pixels
        # always remember to put () here if not , the add will be ok but distance method will not use the correct mass to calculate the center of mass
        # the running average is not the simple one, the running average should be the cumulative  running average, this part is the main idea of this method
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
