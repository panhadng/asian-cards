from cards.cards import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name}'s hand"


class OngDu:
    def __init__(self, num_players):
        self.deck = Deck()
        self.num_players = num_players
        self.players = {f'Player {i}': Player(
            f'Player {i}') for i in range(1, num_players + 1)}
        self.dealer = Player('Dealer')

    def deal_cards(self):
        # Deal 6 cards to each player
        for player in self.players.values():
            player.hand = self.deck.draw_cards(6)

        # Deal 6 cards to the dealer
        self.dealer.hand = self.deck.draw_cards(6)
        return {"Players": self.players, "Dealer": self.dealer.hand}
