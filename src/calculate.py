from sim import Sim
from hand import Hand
from river import River
from deck import Deck
import random

num_iterations = 100000

def hello_world():
    print("hi")

def get_equity(sim: Sim):
    num_hand_1_wins = 0
    num_hand_2_wins = 0
    num_ties = 0
    for i in range(num_iterations):
        new_river = get_randomized_full_river(sim.get_deck(), sim.get_river())
        new_sim = Sim(sim.get_hand_1(), sim.get_hand_2(), new_river)
        winning_hand = new_sim.get_winner()
        if winning_hand == sim.get_hand_1():
            num_hand_1_wins += 1
        elif winning_hand == sim.get_hand_2():
            num_hand_2_wins += 1
        else:
            num_ties += 1
    print("Hand 1 wins " + str(num_hand_1_wins*100/num_iterations) + "percent of the time")
    print("Hand 2 wins " + str(num_hand_2_wins*100/num_iterations) + "percent of the time")
    print("Ties happen  " + str(num_ties*100/num_iterations) + "percent of the time")

def get_randomized_full_river(deck: Deck, river: list):
    new_river = river.get_copy()
    new_deck = deck.get_shuffled_copy()
    while new_river.get_length() < 5:
        new_river.add_card(new_deck.pop_card())
    return new_river