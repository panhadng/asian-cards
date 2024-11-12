from cards.cards import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.can_draw = True

    def draw_card(self, card):
        # Check if the player can draw
        if not self.can_draw:
            raise ValueError(f"{self.name} cannot draw more cards.")
        self.hand.append(card)

    def presentation(self):
        return f"{self.name}'s hand: {self.hand}."

    def __str__(self):
        return self.presentation()

    def __repr__(self):
        return self.presentation()


class Pok:
    def __init__(self, num_players):
        self.deck = Deck()
        self.num_players = num_players
        self.players = {f'Player {i}': Player(
            f'Player {i}') for i in range(1, num_players + 1)}
        self.dealer = Player('Dealer')

    def deal_cards(self):
        # Deal 2 cards to each player
        for player in self.players.values():
            player.hand = self.deck.draw_cards(2)

        # Deal 2 cards to the dealer
        self.dealer.hand = self.deck.draw_cards(2)
        return {"Players": self.players, "Dealer": self.dealer.hand}

    def draw_card(self, player_name):
        # Check if the player is in the game
        if player_name not in self.players and player_name != 'Dealer':
            raise ValueError(f"{player_name} not found.")

        # Check if the dealer can draw
        if player_name == 'Dealer':
            if self.dealer.can_draw:
                card = self.deck.draw_cards(1)
                self.dealer.hand.append(card)
            return self.dealer.hand  # Return the dealer's hand
        else:
            # Check if the player can draw
            if self.players[player_name].can_draw:
                card = self.deck.draw_cards(1)
                self.players[player_name].hand.append(card)
            return self.players[player_name].hand  # Return the player's hand
