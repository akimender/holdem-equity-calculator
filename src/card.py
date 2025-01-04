class Card:
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit
    
    def get_rank(self) -> int:
        return self.rank
    
    def get_suit(self) -> str:
        return self.suit
    
    def __str__(self):
        print(self.rank, self.suit)

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False