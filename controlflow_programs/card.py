import stdio
import stdrandom

# Set rank to a random integer from 2 to 14
rank = stdrandom.uniformInt(2, 15)

# Set rankStr to a string corresponding to rank by using the if statement, and write in standard output if meet the condition
if rank <=10:
    stdio.write(str(rank) + " of ")
elif rank == 11:
    stdio.write("Jack" + " of ")
elif rank == 12:
    stdio.write("Queen" + " of ")
elif rank == 13:
    stdio.write("King" + " of ")
elif rank == 14:
    stdio.write("Ace" + " of ")

# Set suit to a random integer from 1 to 4
suit = stdrandom.uniformInt(1, 5)

# Set suitStr to a string corresponding to suit, and write in standard output if meet the condition
if suit == 1:
    stdio.write("Clubs")
elif suit == 2:
    stdio.write("Diamonds")
elif suit == 3:
    stdio.write("Hearts")
elif suit == 4:
    stdio.write("Spades")


