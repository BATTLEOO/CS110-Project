import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    x = float(sys.argv[1])
    stdio.writeln(_sin(math.radians(x)))


# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def _sin(x):
    # initialize total to 0.0, term to 1.0, sign to 1, and i to 1
    total = 0.0
    term = 1.0
    sign = 1
    i = 1

    # create a while loop as long as total is not equal to total + term , we keep running the loop
    while total != total + term:

        # when x is 60 i is 1 , return 60, what is actually the first value in the formular
        # 60/1 * 60/2 is the second loop which is not odd , so we will not use it, and the sign is positive because we do not satisfy the if statement
        # but we still store the value of the second loop, it is useful for the future calculation
        # for the third loop , 60/1 * 60/2 * 60/3, it is the same as 60^3 / 3!(it is 1*2*3), and the sign will be change to minus in the if statement
        term *= x/i

        # create if statement check whether i is odd or not
        if i % 2 != 0:

            # we record the term that is odd and sum it to total, add new sign * term to total
            total = total + sign * term

            # write sign = -sign, sign is changing every new loop, it can be see directly in the formular

            sign = -sign

        # increment i by 1
        i += 1

    # return total, the value that we want
    return total


if __name__ == "__main__":
    main()
