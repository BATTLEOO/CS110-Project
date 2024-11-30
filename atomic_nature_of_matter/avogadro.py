import math
import stdio


# Entry point.
def main():
    # ETA is viscosity of water, Initialize ETA = 9.135e-4
    ETA = 9.135e-4

    # RHO is the radius of bead, Initialize RHO = 0.5e-6
    RHO = 0.5e-6

    # T is absolute temperature, Initialize T = 297
    T = 297

    # R is universal gas constant, Initialize R = 8.31457
    R = 8.31457

    # set n to zero, serve as counter
    n = 0

    # set var_numerator = 0.0
    var_numerator = 0.0

    # create while not stdio.isEmpty(), the loop stop when there is no standard input
    while not stdio.isEmpty():
        # read input, assign input to displacement, use stdio.readFloat to check the number one by one
        displacements = stdio.readFloat()

        # covert pixels to meters, use the formular provided (displacements * 0.175e-6)
        displacements = displacements * 0.175e-6

        # Calculate var_numerator as the sum of the squares of the n displacements
        var_numerator += displacements ** 2

        # increment n by 1, record the number of time we iterate
        n += 1

    # calculate var, Divide var by 2 * n, remember to put() when 2 * n, if not the result will be wrong
    var = var_numerator / (2 * n)

    # Estimate Boltzmann’s constant (assign the value to k) as 6 * math.pi * var * ETA * RHO / T
    k = 6 * math.pi * ETA * RHO * var / T

    # Estimate Avogadro’s constant(assign the value to Na) as R / k
    Na = R / k

    # Write to standard output the Avogadro constant in scientific notation (using the format string "%e")
    stdio.writef('%.6e\n', Na)

    # For run code: py bead_tracker.py 25 180.0 25.0 data/run_1/* | py avogadro.py



if __name__ == "__main__":
    main()
