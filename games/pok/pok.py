from cards.cards import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.can_draw = True

    def draw_card(self, card):
        self.hand.append(card)


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

    def calculate_score(self, hand):
        # Define the ongs and bomber
        ongs = ['king', 'queen', 'jack']
        bomber = ['8', '9']

        # Calculate the score based on the rules provided
        score = sum(0 if card.value.lower() in ongs else 1 if card.value.lower(
        ) == 'ace' else int(card.value) for card in hand) % 10

        # Check for bomb condition
        is_bomb = len(hand) == 2 and all(
            card.value in bomber for card in hand)

        # Check for three ongs condition
        is_three_ongs = len(hand) == 3 and all(
            card.value.lower() in ongs for card in hand)

        # Check for three of a kind condition
        is_three_of_a_kind = len(hand) == 3 and len(
            set(card.value for card in hand)) == 1

        # Calculate the multiplier based on the suits
        suits = {}
        for card in hand:
            suit = card.suit  # Assuming card has a 'suit' attribute
            suits[suit] = suits.get(suit, 0) + 1

        # Set the multiplier based on the conditions
        if is_three_ongs:
            multi = 3
        elif is_three_of_a_kind:
            multi = 5
        else:
            multi = 1  # Default multiplier
            if 3 in suits.values():
                multi = 3
            elif 2 in suits.values() and len(hand) == 2:
                multi = 2

        result = {
            "score": score,
            "multi": multi,
            "is_bomb": is_bomb,
            "is_three_ongs": is_three_ongs,
            "is_three_of_a_kind": is_three_of_a_kind
        }

        # Return the result
        return result

    def draw_card(self, player_name):
        if player_name not in self.players and player_name != 'Dealer':
            raise ValueError(f"{player_name} not found.")

        if player_name == 'Dealer':
            if self.dealer.can_draw:
                card = self.deck.draw_cards(1)
                self.dealer.hand.append(card)
        else:
            if self.players[player_name].can_draw:
                card = self.deck.draw_cards(1)
                self.players[player_name].hand.append(card)

    def start(self):
        self.deal_cards()
        return {"Players": self.players, "Dealer": self.dealer.hand}
