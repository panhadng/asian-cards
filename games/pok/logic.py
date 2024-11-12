from enum import IntEnum


class HandRank(IntEnum):
    NORMAL = 0
    THREE_ONGS = 1
    THREE_OF_A_KIND = 2
    JACKPOT = 3


class Result:
    def __init__(self, winner, loser, is_tie, multi):
        self.winner = winner
        self.loser = loser
        self.is_tie = is_tie
        self.multi = multi

    def presentation(self):
        if self.is_tie:
            return f"It is a tie game."
        else:
            self.multi = calculate_score(self.winner.hand)['multi']
            return f"{self.winner.name} beats {self.loser.name} with a multiplier of {self.multi}."

    def __str__(self):
        return self.presentation()

    def __repr__(self):
        return self.presentation()


def calculate_score(hand):
    # Define the ongs and jackpots
    ongs = ['king', 'queen', 'jack']
    jackpots = [8, 9]

    # Calculate the score based on the rules provided
    score = sum(0 if card.value.lower() in ongs else 1 if card.value.lower(
    ) == 'ace' else int(card.value) for card in hand) % 10

    # Check for jackpot condition
    is_jackpot = len(hand) == 2 and score in jackpots

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
        elif len(hand) == 2 and len(set([card.value for card in hand])) == 1:
            multi = 2

    # Determine hand rank
    rank = HandRank.NORMAL
    if is_jackpot:
        rank = HandRank.JACKPOT
    elif is_three_of_a_kind:
        rank = HandRank.THREE_OF_A_KIND
    elif is_three_ongs:
        rank = HandRank.THREE_ONGS

    # Return the result
    result = {
        "score": score,
        "multi": multi,
        "rank": rank,
        "is_jackpot": is_jackpot,
        "is_three_ongs": is_three_ongs,
        "is_three_of_a_kind": is_three_of_a_kind
    }
    return result


def compare_hands(player_one, player_two):
    score_one = calculate_score(player_one.hand)
    score_two = calculate_score(player_two.hand)
    result = Result(None, None, False, 1)

    # Compare ranks first
    if score_one['rank'] != score_two['rank']:
        if score_one['rank'] > score_two['rank']:
            result.winner, result.loser = player_one, player_two
        else:
            result.winner, result.loser = player_two, player_one
        return result

    # If same rank, compare scores
    if score_one['score'] > score_two['score']:
        result.winner, result.loser = player_one, player_two
    elif score_one['score'] < score_two['score']:
        result.winner, result.loser = player_two, player_one
    else:
        result.is_tie = True
    return result
