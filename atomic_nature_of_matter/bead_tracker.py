import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # create command line arguments pixels(int), tau(float), delta(float)
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    # create a frame as empty list in order to store a sequence of image frames
    # using 4: to include all the input after argument 3, this also help to read the file name
    frames = list(sys.argv[4:])

    # Construct a BlobFinder object for the frame and set the picture frame to frames[0]
    # here is to initial blobs, use BlobFinder on the first frame to identify blobs
    # frames[0] means the first input in sys.argv[4:]
    object_frame = BlobFinder(Picture(frames[0]), tau)

    # from object_frame get a list of beads prev_beads that have at least pixels(user input)
    prev_beads = object_frame.getBeads(pixels)

    # For each frame starting at sys.argv[5]:
    # sys.argv[5:] means read all the input after sys.argv[4], sys.argv property is list so can use the slicing method
    # set for loop to iterate subsequent_frame starting at object_frame
    for subsequent_frame in sys.argv[5:]:

        # Construct a BlobFinder object(blob_detect) and from it get a list of beads currBeads (store in curr_beads) that have at least pixels
        blob_detect = BlobFinder(Picture(subsequent_frame), tau)
        curr_beads = blob_detect.getBeads(pixels)

        # for curr_bead in curr_beads
        for curr_bead in curr_beads:

            # use map lambda: it is more clean and organize to use map lambda to calculate a list of prev_beads
            distance = map(lambda prev: curr_bead.distanceTo(prev), prev_beads)

            # use the filter to create a one time if statement to find the value x < = delta as a list
            closest_distance = list(filter(lambda dis: dis <= delta, distance))

            # if closest_distance is ture
            if closest_distance:

                # use min: because closest_distance is list, and we only want one value that is the closest_distance
                # the closest_distance means that the smaller the distance is, the closer we are
                # so use min to find the value that we want, and min also help to change our data type from list to float
                closest_distance = min(closest_distance)

                # write the output in standard format '%.4f\n'
                stdio.writef('%.4f\n',closest_distance)

        # Write a newline character
        stdio.writeln()

        # Set prevBeads to currBeads (update the curr_beads to prev_beads)

        prev_beads = curr_beads

if __name__ == "__main__":
    main()

#py bead_tracker.py 25 180.0 25.0 data/run_1/frame00000.jpg data/run_1/frame00001.jpg