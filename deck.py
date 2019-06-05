# Project 3b 
# Anna Markiewicz
# May 12
# deck.py


# Shuffle the Card objects in the deck
import random

from card import Card

class Deck:
    """Card Deck, which takes self as input, and creates a deck of cards
    """

    def __init__(self):
        self.cards = [ ]
        for suit in ['C', 'D', 'H', 'S']:
            for rank in range(2,15):
                # print(f"I am creating suit = {suit}, rank = {rank}")
                # create a new card with the specified rank
                # and suit and append it to the list. 
                self.cards.append(Card(rank, suit))

    def __str__(self):
        output = ""
        # Concatenate card to 
        # the output variable
        for card in self.cards:
            output = output + str(card) + " "
        return output

    def __repr__(self):
        return str(self)

    def shuffle(self):
        # print("I am shuffling cards...")
        random.shuffle(self.cards) 

    def deal_card(self):
        # # Remove the card from the top of the cards list and save it as the Card object c
        # print (len(self.cards))
        # print("I am popping one card...")
        return self.cards.pop()

    def pop_card(self):
        # # Remove the card from the top of the cards list and save it as the Card object c
        # print (len(self.cards))
        # print("I am popping one card...")
        return self.cards.pop()

    def count_cards(self):
        # print("I am counting cards...")
        return (len(self.cards))

    def is_empty(self):
        if not self.cards:
            return True
        else:
            return False

    def add_to_top(self, rank, suit):
        # Create a new card with the specified rank and suit and append it to the cards in the deck
        c = Card(rank, suit)
        self.cards.append(c)
        return self.cards[-1]

    def add_to_bottom(self, rank, suit):
        # Insert the card c at the bottom of the deck (before the item with index 0)
        c = Card(rank, suit)
        self.cards.insert(0, c)
        return self.cards[0]







    

if (__name__) == '__main__':
    deck = Deck()

    #print(f"deck.cards = {deck.cards[7]}")

    # for card in deck.cards:
    #     print(card)
    deck.shuffle()
    print(deck)
    deck.deal_card()
    print(deck.deal_card())
    deck.pop_card()
    print(deck.pop_card())
    deck.count_cards()
    print(deck.count_cards())
    deck.is_empty()
    print(deck.is_empty())

    c = Card(10, "H")
    deck.add_to_top(10, "H")
    print(deck.add_to_top(10, "H"))

    c = Card(8, "C")
    deck.add_to_bottom(8, "C")
    print(deck.add_to_bottom(8, "C"))


