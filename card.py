class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def display(self):
        """Returns the ASCII representation of the card."""
        symbol = self.suit_symbols[self.suit]
        rank = f"{self.rank:<2}"  # Left-aligned with at least 2 characters
        return [
            "┌───────┐",
            f"│ {rank}    │",
            "│       │",
            f"│   {symbol}   │",
            "│       │",
            f"│    {rank} │",
            "└───────┘",
        ]
