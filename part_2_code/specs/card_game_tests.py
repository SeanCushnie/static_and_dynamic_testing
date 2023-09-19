import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Ace", 1)
        self.card2 = Card("King", 13)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        result = CardGame().check_for_ace(self.card1)
        self.assertTrue(result)

    def test_for_highest_card(self):
        result = CardGame().highest_card(self.card1, self.card2)
        self.assertEqual(self.card2,result)

    def test_cards_total(self):
        cards = self.cards
        result = str(CardGame().cards_total(cards))
        self.assertEqual("You have a total of 14", result)
    

