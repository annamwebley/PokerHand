# Project 5 
# Anna Markiewicz
# June 6
# test2a.py

from card import Card 
import unittest

class TestCard(unittest.TestCase):

    def test_card(self):
        my_first_card = Card(12, "S")
        self.assertEqual(str(my_first_card), "QS")

    def test_card_suit(self):
        result = Card(12, "S")
        self.assertEqual(result.suit, "S")

    def test_card_rank(self):
        result = Card(12, "S")
        self.assertEqual(result.rank, 12)

    def test_strongest_card(self):
        strongest_card = Card(14, "S")
        self.assertEqual(str(strongest_card), "AS")

    def test_weakest_card(self):
        weakest_card = Card(2, "C")
        self.assertEqual(str(weakest_card), "2C")

    def test_color_black(self):
        result_black = Card(5, "S")
        self.assertEqual(result_black.color(), "black")

    def test_color_red(self):
        result_red = Card(3, "H")
        self.assertEqual(result_red.color(), "red")

    def test__lt__True(self):
        print(f"*"*80)
        c = Card(11, "S")
        d = Card(8, "H")
        actual_result = d < c
        expected_result = True
        print(f"I am testing __lt__True")
        print(f"The expected_result = {expected_result}")
        print(f"The actual_result = {actual_result}")


    def test__lt__False(self):
        print(f"*"*80)
        c = Card(11, "S")
        d = Card(8, "H")
        actual_result = d > c
        expected_result = False
        print(f"I am testing __lt__False")
        print(f"The expected_result = {expected_result}")
        print(f"The actual_result = {actual_result}")

    def test__eq__True(self):
        print(f"*"*80)
        c = Card(2, "D")
        d = Card(6, "H")
        actual_result = d = c
        expected_result = True
        print(f"I am testing __eq__True")
        print(f"The expected_result = {expected_result}")
        print(f"The actual_result = {actual_result}")

    def test__eq__False(self):
        print(f"*"*80)
        c = Card(2, "D")
        d = Card(6, "H")
        actual_result = d = c
        expected_result = False
        print(f"I am testing __eq__False")
        print(f"The expected_result = {expected_result}")
        print(f"The actual_result = {actual_result}")




if __name__ == "__main__":
    unittest.main()