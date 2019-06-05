# Project 5 
# Anna Markiewicz
# June 6
# test2b.py

from card import Card
from deck import Deck
from pokerhand import PokerHand
from constants import *
# import unittest


my_first_card = Card(5, "D")
print(f"the result is: {my_first_card}")
print(f"the color is: {my_first_card.color()}")

my_second_card = Card(2, "S")
print(f"the result is: {my_second_card}")
print(f"the color is: {my_second_card.color()}")


my_third_card = Card(3, "H")
print(f"the result is: {my_third_card}")
print(f"the color is: {my_third_card.color()}")

print(f"Starting tests for poker hand...")
deck = Deck()
the_array = [
    Card(2, "H"), 
    Card(2, "D"),
    Card(2, "S"),
    Card(2, "C"),
    Card(4, "H"),
    ]




# for i in range(0,5):
#     the_array.append(deck.deal_card())
print(the_array)
rigged_four_of_a_kind = PokerHand(the_array)
rigged_four_of_a_kind.classify()
print(rigged_four_of_a_kind.hand_type)