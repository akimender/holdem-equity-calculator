from card import Card
from deck import Deck
from hand import Hand
from river import River

class Sim:

    def __init__(self, hand_1: Hand, hand_2: Hand, river=River()):
        self.deck = Deck()
        self.hand_1 = hand_1
        self.hand_2 = hand_2
        self.river = river
        self.deck.remove_hand_cards(hand_1)
        self.deck.remove_hand_cards(hand_2)
        self.deck.remove_river_cards(river)
    
    def get_winner(self) -> Hand:
        hand_1_score = self.evaluate_hand(self.hand_1, self.river)
        hand_2_score = self.evaluate_hand(self.hand_2, self.river)

        print("hand 1 score", hand_1_score)
        print("hand 2 score", hand_2_score)

        if hand_1_score > hand_2_score:
            print("Hand 1 wins!")
            return self.hand_1
        elif hand_1_score < hand_2_score:
            print("Hand 2 wins!")
            return self.hand_2
        print("Tie!")
        return None
    
    def evaluate_hand(self, hand: Hand, river: River) -> int: # returns range from 100 to 1000
        cards = hand.get_cards() + river.get_cards() # cards should have 7 cards
        
        ranks = []
        suits = []

        for card in cards:
            ranks.append(card.get_rank())
            suits.append(card.get_suit())
        
        # running helper methods below

        ### HELPER METHODS for evaluate_hand method ###

        def test_straight_flush() -> int:
            suit_dict = {}

            for card in cards:
                suit = card.get_suit()
                if suit in suit_dict:
                    suit_dict[suit].append(card)
                else:
                    suit_dict[suit] = [card]

            for suit in suit_dict:
                if len(suit_dict[suit]) >= 5:
                    sorted_cards = sorted(suit_dict[suit], key=lambda card: card.rank)
                    consecutive_count = 1

                    for i in range(1, len(sorted_cards)):
                        if sorted_cards[i].get_rank() == sorted_cards[i - 1].get_rank() + 1 or (sorted_cards[i - 1].get_rank() == 13 and sorted_cards[i].get_rank() == 1):
                            consecutive_count += 1
                            if consecutive_count >= 5:
                                return 800 + sorted_cards[i].get_rank()
            return -1

        # returns highest integer if the ranks has a straight
        # returns -1 otherwise
        def test_straight() -> int:
            nums = sorted(set(ranks))
            consecutive_count = 1

            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1] + 1 or (nums[i - 1] == 13 and nums[i] == 1):
                    consecutive_count += 1
                    if consecutive_count >= 5:  # If we find 5 consecutive numbers, return True
                        return 400 + nums[i]
                else:
                    consecutive_count = 1
            
            return -1
        
        def test_flush() -> int:
            suit_dict = {} # dictionary approach to tracking frequencies of suits
            flush_suit = None
            for card in cards:
                suit = card.get_suit()
                if suit in suit_dict:
                    suit_dict[suit].append(card)
                else:
                    suit_dict[suit] = [card]
                
                if len(suit_dict[suit]) >= 5:
                    flush_suit = suit
            
            if flush_suit:
                max_rank = -1
                for card in suit_dict[flush_suit]:
                    if card.get_rank() > max_rank:
                        max_rank = card.get_rank()
                return 500 + max_rank
            else:
                return -1

        def test_quads() -> int:
            rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
            quads = [rank for rank, count in rank_count.items() if count == 4]

            if quads:
                return 700 + quads[0]
            return -1

        def test_full_house() -> int:
            rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
            three_of_kind = [rank for rank, count in rank_count.items() if count == 3]
            pairs = [rank for rank, count in rank_count.items() if count == 2]

            # scoring logic here doesnt tiebreak for matching three of a kind and mismatched two of a kind
            # NEEDS FIXING
            if three_of_kind and pairs:
                return 600 + three_of_kind[0]
            elif len(three_of_kind) > 1:
                return 600 + max(three_of_kind)
            return -1
        
        def test_trips() -> int:
            rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
            trips = [rank for rank, count in rank_count.items() if count == 3]

            if trips:
                return 300 + trips[0]
            return -1

        def test_two_pair() -> int:
            rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
            pairs = [rank for rank, count in rank_count.items() if count == 2]

            if len(pairs) >= 2:
                return 200 + max(pairs)
            return -1

        def test_one_pair() -> int:
            rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
            pairs = [rank for rank, count in rank_count.items() if count == 2]

            if pairs:
                return 100 + max(pairs)
            return -1

        def test_high_card() -> int:
            return max(ranks)
        
        ### running helper methods ###

        if test_straight_flush() > -1:
            return test_straight_flush()
        elif test_quads() > -1:
            return test_quads()
        elif test_full_house() > -1:
            return test_full_house()
        elif test_flush() > -1:
            return test_flush()
        elif test_straight() > -1:
            return test_straight()
        elif test_trips() > -1:
            return test_trips()
        elif test_two_pair() > -1:
            return test_two_pair()
        elif test_one_pair() > -1:
            return test_one_pair()
        return test_high_card()