class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand = cards

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def display_hand(self):
        """Displays the player's hand in a terminal-friendly card format."""
        if not self.hand:
            return
        card_lines = [card.display() for card in self.hand]
        for i in range(7):  # Each card has 7 lines
            print("  ".join(card[i] for card in card_lines))
