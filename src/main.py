from sim import Sim
from hand import Hand
from card import Card
from river import River
from calculate import *

sim_1 = Sim(Hand(Card(13, "Hearts"), Card(13, "Spades")),
            Hand(Card(12, "Hearts"), Card(12, "Clubs")),
            River())

get_equity(sim_1)