import stdarray
import stdio
import sys
from blob import Blob
from color import Color
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):

        # create an empty list to store the bead we fund, self._blobs = []
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same dimensions as pic
        # use pic.width() and pic.height() to get col and row, (Notice: make row to width, and col to height)
        marked = stdarray.create2D(pic.width(), pic.height())

        # for each col of the image (pic.width())
        for i in range(pic.width()):

            for j in range(pic.height()):  # for through each row of the image (pic.height())

                #  create a Blob object called blob, we can see this blob as a temporary container
                blob = Blob()

                #  call _findBlob() with the appropriate arguments (the method that defined)
                self._findBlob(pic, tau, i, j, marked, blob)

                # if statement when blob.mass() > 0 ,  add blob to self._blobs
                if blob.mass() > 0:
                    self._blobs += [blob]

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        # create an empty list to store the value of our beads
        all_beads = []

        # self._blobs have all the blobs that we found, and we want to count
        # To know how many beads we have, use for loop to go through self._blobs
        for b in self._blobs:

            # we call mass (it return pixels to use), we only want the value that is bigger that pixels
            if b.mass() >= pixels:

                # add b to add_beads
                all_beads += [b]

        # Return a list of blobs from blobs that have a mass ≥ pixels
        return all_beads

    ## Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    ## threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    ## being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        #  Base case: return if pixel (i, j) is out of bounds, or if it is marked, or if its luminance (use the luminance() method from Color for this) is less than tau.
        #  Can call Color directly because luminance is Static methods: independent of any instance of the class (can be use directly without creating object)
        if i < 0 or i >= pic.width() or j < 0 or j >= pic.height() or marked[i][j] == True or Color.luminance(pic.get(i, j)) < tau:
            return

        # marked[i][j], make the current position True
        marked[i][j] = True

        # call blob add pixel(i , j), to get the new center mass
        blob.add(i, j)

        # remember i is column , j is row
        # when j - 1 means N
        self._findBlob(pic, tau,i , j - 1, marked, blob)

        # when j + 1 means S
        self._findBlob(pic, tau, i, j + 1, marked, blob)

        # when i - 1 means E
        self._findBlob(pic, tau, i - 1, j, marked, blob)

        # when i + 1 means W
        self._findBlob(pic, tau, i + 1, j, marked, blob)




# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == "__main__":
    _main()

# For run code: py blob_finder.py 25 180.0 data/run_1/frame00001.jpg
