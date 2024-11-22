from pygame.gfxdraw import pixel

import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        self._blobs = []
        self._pic = Picture(pic)
        self._tau =
        # something wrong is happening here
        # Notice: check the import statement , what I can use from it, need to think about it
        self.marked = stdarray.create2D(rowCount=pic,colCount=pic)
        for i in range(pic):
            for each pixel(i, j):
                blob = Blob()
                _findBlob()
                if blob.mass() > 0:
                    self._blobs += blob
                    # should i use the add method in blob?


    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        lis = Blob(self)
        if lis.mass >= pixels:
            return lis

    ## Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    ## threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    ## being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        # how do i know pixel(i, j) is out of bounds
        if pixel(i, j) != True or marked or Color.luminance() < tau:
            return
        marked += pixel(i, j)
        blob += pixel(i, j)
        self._findBlob() if N, S, W, S is pixel



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

# py blob_finder.py 25 180.0 data/run_1/frame00001.jpg
