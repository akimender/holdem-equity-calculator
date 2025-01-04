from card import Card
from hand import Hand
from river import River
import random

class Deck:
    cards = []

    def __init__(self):
        self.generate_new_deck()

    # sets cards to a new shuffled Deck of cards
    def generate_new_deck(self):
        self.cards.clear()
        for i in range(1, 14): # i in 1-13
            self.cards.append(Card(i, "Spades"))
            self.cards.append(Card(i, "Clubs"))
            self.cards.append(Card(i, "Diamonds"))
            self.cards.append(Card(i, "Hearts"))
        random.shuffle(self.cards)

    def get_card(self) -> Card:
        return self.cards.pop()
    
    def add_card(self, card: Card):
        self.cards.append(card)
    
    def get_all_cards(self) -> list:
        return self.cards
    
    def remove_card(self, card: Card):
        self.cards.remove(card)

    def remove_hand_cards(self, hand: Hand):
        for card in hand.get_cards():
            self.cards.remove(card)
    
    def remove_river_cards(self, river: River):
        for card in river.get_cards():
            self.cards.remove(card)