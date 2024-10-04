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
        return f"{self.name}'s hand: {self.hand}"

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
        else:
            # Check if the player can draw
            if self.players[player_name].can_draw:
                card = self.deck.draw_cards(1)
                self.players[player_name].hand.append(card)

        # Return the player's hand
        return self.players[player_name].hand


def calculate_score(hand):
    # Define the ongs and bomber
    ongs = ['king', 'queen', 'jack']
    bomber = [8, 9]

    # Calculate the score based on the rules provided
    score = sum(0 if card.value.lower() in ongs else 1 if card.value.lower(
    ) == 'ace' else int(card.value) for card in hand) % 10

    # Check for bomb condition
    is_bomb = len(hand) == 2 and score in bomber

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

    # Return the result
    result = {
        "score": score,
        "multi": multi,
        "is_bomb": is_bomb,
        "is_three_ongs": is_three_ongs,
        "is_three_of_a_kind": is_three_of_a_kind
    }
    return result


def compare_hands(hand1, hand2):
    score_info1 = calculate_score(hand1)
    score_info2 = calculate_score(hand2)

    # Compare based on the ranking criteria
    if score_info1['is_bomb'] and score_info2['is_bomb']:
        # If both are bombs, compare scores
        if score_info1['score'] > score_info2['score']:
            return "Hand 1 wins"
        elif score_info1['score'] < score_info2['score']:
            return "Hand 2 wins"
        else:
            return "It's a tie"

    if score_info1['is_bomb'] and not score_info2['is_bomb']:
        return "Hand 1 wins"
    elif score_info2['is_bomb'] and not score_info1['is_bomb']:
        return "Hand 2 wins"
    elif score_info1['multi'] == 5 and score_info2['multi'] != 5:
        return "Hand 1 wins"
    elif score_info2['multi'] == 5 and score_info1['multi'] != 5:
        return "Hand 2 wins"
    elif score_info1['is_three_ongs'] and not score_info2['is_three_ongs']:
        return "Hand 1 wins"
    elif score_info2['is_three_ongs'] and not score_info1['is_three_ongs']:
        return "Hand 2 wins"
    elif score_info1['score'] > score_info2['score']:
        return "Hand 1 wins"
    elif score_info1['score'] < score_info2['score']:
        return "Hand 2 wins"
    else:
        return "It's a tie"
