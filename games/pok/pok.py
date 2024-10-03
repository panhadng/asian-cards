from cards.cards import Deck


class Pok:
    def __init__(self, num_players):
        self.deck = Deck()
        self.num_players = num_players
        self.hands = {}
        self.dealer_hand = {}

    def deal_cards(self):
        # Deal 2 cards to each player
        for player in range(1, self.num_players + 1):
            self.hands[f'Player {player}'] = self.deck.draw_cards(2)

        # Deal 2 cards to the dealer
        self.dealer_hand = self.deck.draw_cards(2)

    def start(self):
        self.deal_cards()
        # Return hands for players and dealer for verification
        return {"Players": self.hands, "Dealer": self.dealer_hand}
