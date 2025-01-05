from card import Card
import copy

class River:
    def __init__(self, current_cards=[]):
        self.cards = current_cards or []

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_cards(self) -> list:
        return self.cards
    
    def get_copy(self):
        return copy.deepcopy(self)
    
    def get_length(self):
        return len(self.cards)