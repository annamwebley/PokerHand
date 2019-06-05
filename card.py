# Project 3a 
# Anna Markiewicz
# May 1
# card.py

class Card:
    """
    Takes rank and suit as input, and returns card object. Typical use: 
    card = Card(int, str) for example, c = Card(11, "S")
     """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        symbols = ["", "", "2", "3", "4", "5", "6", "7", 
            "8", "9", "10", "J", "Q", "K", "A"]
        return symbols[self.rank] + self.suit

    def __repr__(self):
        return str(self)


    def color(self):
        if self.suit == "C":
            return "black"
        elif self.suit == "S":
            return "black"
        elif self.suit == "D":
            return "red"
        elif self.suit == "H":
            return "red"
        else:
            return "option does not exist"

    def __lt__(self, other):
        self.rank < other.rank

    def __eq__(self, other):
        self.rank == other.rank



if __name__ == "__main__":

    c = Card(11, "S")
    print(f"the letter is: {c.suit}")
    print(f"the color is: {c.color()}")

