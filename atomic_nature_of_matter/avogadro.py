import math
from lib2to3.pytree import convert

import stdio


# Entry point.
def main():
    # ETA is viscosity of water
    ETA = 9.135e-4

    # RHO is the radius of bead
    RHO = 0.5e-6

    # T is absolute temperature
    T = 297

    # R is universal gas constant
    R = 8.31457

    n = 0
    var_numerator = 0.0
    while not stdio.isEmpty():
        # read input
        displacements = stdio.readFloat()
        # covert pixels to meters
        displacements = displacements * 0.175e-6
        # calculate var numerator by square each of them as sum
        var_numerator += displacements ** 2
        # record the number of time we iterate
        n += 1

    # calculate var, problem fixed , have to remember to put() when 2 * n, if not the result will be wrong
    var = var_numerator / (2 * n)

    # not using anything from blob just the data import from bead_tracker

    k = 6 * math.pi * ETA * RHO * var / T

    Na = R / k

    stdio.writef('%.6e\n', Na)

    # py bead_tracker.py 25 180.0 25.0 data/run_1/* | py avogadro.py



if __name__ == "__main__":
    main()
