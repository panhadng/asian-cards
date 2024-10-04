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
