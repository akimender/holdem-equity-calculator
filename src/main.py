from sim import Sim
from hand import Hand
from card import Card
from river import River

hand_1 = Hand(Card(1, "Hearts"), Card(11, "Spades"))
hand_2 = Hand(Card(6, "Diamonds"), Card(7, "Diamonds"))
river = River([Card(2, "Hearts"), Card(3, "Clubs"), Card(5, "Spades"), Card(11, "Clubs"), Card(12, "Diamonds")])

sim = Sim(hand_1, hand_2, river)

sim.get_winner()