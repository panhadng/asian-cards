import requests


class Deck:
    def __init__(self, deck_count=1):
        self.api_url = "https://deckofcardsapi.com/api/deck/"
        self.deck = self.shuffle(deck_count)
        self.deck_id = self.deck['deck_id']
        self.remaining = self.deck['remaining']

    def shuffle(self, deck_count):
        url = f"{self.api_url}/new/shuffle/?deck_count={deck_count}"
        response = requests.get(url)
        deck = response.json()
        return deck

    def draw_cards(self, count=1):
        if self.remaining < count:
            raise ValueError("Not enough cards remaining in the deck.")
        url = f"{self.api_url}/{self.deck_id}/draw/?count={count}"
        response = requests.get(url)
        cards_data = response.json()
        self.remaining -= count
        if count == 1:
            return Card(cards_data['cards'][0])
        else:
            return [Card(card) for card in cards_data['cards']]

    def __str__(self):
        return f"Deck is shuffled with ID of {self.deck_id} and {self.deck['remaining']} cards remaining."


class Card:
    def __init__(self, card):
        self.code = card['code']
        self.image = card['image']
        self.images = card['images']
        self.value = card['value']
        self.suit = card['suit']

    def __str__(self):
        return f"{self.value} of {self.suit}"
