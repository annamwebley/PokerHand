# Project 5 
# Anna Markiewicz
# June 6
# card.py

from card import Card
from deck import Deck
from constants import *

class PokerHand(Deck):

    def __init__(self, the_array):
        self._cards = []
        self.hand_type = "UNCLASSIFIED"
        # print(f"I am inside pokerhand...{the_array}")
        for card in the_array:
            self._cards.append(card)

    def classify(self):
        self._cards.sort( )
        print(f"Classify cards = {self._cards}")
        print(f"Classify cards[0] = {self._cards[0]}")
        print(f"Classify cards[1] = {self._cards[1]}")

        # if False:
        #     pass # ... code to classify hand of type STRAIGHT_FLUSH:

        if self._cards[0] == self._cards[1] and \
            self._cards[1] == self._cards[2] and \
            self._cards[2] == self._cards[3]:

            self.hand_type = FOUR_OF_A_KIND

        elif self._cards[1] == self._cards[2] and \
            self._cards[2] == self._cards[3] and \
            self._cards[3] == self._cards[4]:

            self.hand_type = FOUR_OF_A_KIND
            
        elif False:
            pass# ... code to classify hand of type FULL_HOUSE:

        elif False:
            pass # ... code to classify hand of type FLUSH:

        elif False:
            pass # ... code to classify hand of type STRAIGHT:

        elif False:
            pass # ... code to classify hand of type THREE_OF_A_KIND:

        elif False:
            pass # ... code to classify hand of type TWO_PAIR:

        elif False:
            pass # ... code to classify hand of type ONE_PAIR:
        
        else:
            self.hand_type = NO_PAIR

        


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    the_array = []
    for i in range(0,5):
        the_array.append(deck.deal_card())
    print(the_array)
    poker_hand = PokerHand(the_array)