class Card:
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit
    
    def get_rank() -> int:
        global rank
        return rank
    
    def get_suit() -> str:
        global suit
        return suit
    
    def __str__():
        print(rank, suit)

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False