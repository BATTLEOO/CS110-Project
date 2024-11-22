import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    # Construct a BlobFinder object for the frame sys.argv[4] and from it get a list of beads prevBeads that have at least pixels
    frame = BlobFinder(sys.argv[4], tau)
    # For each frame starting at sys.argv[5]:
    currBeads = []
    for frame in range(int(sys.argv[5])):

        # Construct a BlobFinder object and from it get a list of beads currBeads that have at least pixels
        bf = BlobFinder(frame, tau)

        currBeads += [bf]

        #  For each bead currBead in currBeads, find a bead prevBead from prevBeads that is no further than delta and is closest to currBead,
        for currBead in currBeads:
            prevBead = blob_finder(currBead, tau)
            prevBeads = []
            prevBeads += [prevBead]

        #  and if such a bead is found, write its distance (using format string ’%.4f\n’) to currBead
        if frame:

            currBeads = distance

        # Write a newline character
        stdio.writeln()
        # Set prevBeads to currBeads
        prevBeads = currBeads

if __name__ == "__main__":
    main()
