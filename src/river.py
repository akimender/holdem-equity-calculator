from .card import Card

class River:
    cards = []

    def __init__(self, current_cards=None):
        self.current_cards = current_cards or []
        for card in self.current_cards:
            self.cards.append(card)

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_cards(self) -> list:
        return self.cards