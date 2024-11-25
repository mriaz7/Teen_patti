# class Deal:
#     def __init__(self, initial_coins=1000):
#         self.user_coins = initial_coins
#         self.computer_coins = initial_coins
#         self.pot = 0

#     def place_bet(self, player_name, bet_amount):
#         """Deducts coins from a player and adds to the pot."""
#         if player_name == "User":
#             if bet_amount > self.user_coins:
#                 print("You don't have enough coins to place this bet!")
#                 return False
#             self.user_coins -= bet_amount
#         elif player_name == "Computer":
#             if bet_amount > self.computer_coins:
#                 print("Computer doesn't have enough coins to place this bet!")
#                 return False
#             self.computer_coins -= bet_amount

#         self.pot += bet_amount
#         print(f"{player_name} placed a bet of {bet_amount} coins.")
#         return True

#     def distribute_winnings(self, winner_name):
#         """Awards the pot to the winner."""
#         if winner_name == "User":
#             self.user_coins += self.pot
#         elif winner_name == "Computer":
#             self.computer_coins += self.pot

#         print(f"\n{winner_name} wins {self.pot} coins!")
#         self.pot = 0  # Reset the pot after distributing

#     def show_balances(self):
#         """Displays the current coin balances."""
#         print(f"\nCurrent Coin Balances:")
#         print(f"User: {self.user_coins} coins")
#         print(f"Computer: {self.computer_coins} coins")
#         print(f"Pot: {self.pot} coins")

# class Deal:
#     def __init__(self):
#         self.user_coins = 100  # Initial coins for the user
#         self.computer_coins = 100  # Initial coins for the computer
#         self.pot = 0  # Total coins in the pot

#     def show_balances(self):
#         print(f"User Coins: {self.user_coins}")
#         print(f"Computer Coins: {self.computer_coins}")

#     def place_bet(self, player, amount):
#         if player == "User" and self.user_coins >= amount:
#             self.user_coins -= amount
#             self.pot += amount
#             return True
#         elif player == "Computer" and self.computer_coins >= amount:
#             self.computer_coins -= amount
#             self.pot += amount
#             return True
#         return False

#     def distribute_winnings(self, winner):
#         if winner == "User":
#             self.user_coins += self.pot
#         elif winner == "Computer":
#             self.computer_coins += self.pot
#         self.pot = 0  # Reset the pot


class Deal:
    def __init__(self):
        self.user_coins = 1000  # Initial coins for the user
        self.computer_coins = 1000  # Initial coins for the computer
        self.pot = 0  # Total coins in the pot

    def show_balances(self):
        print(f"User Coins: {self.user_coins}")
        print(f"Computer Coins: {self.computer_coins}")
        print(f"Pot: {self.pot}")

    def place_bet(self, player, amount):
        if player == "User" and self.user_coins >= amount:
            self.user_coins -= amount
            self.pot += amount
            return True
        elif player == "Computer" and self.computer_coins >= amount:
            self.computer_coins -= amount
            self.pot += amount
            return True
        return False

    def distribute_winnings(self, winner):
        if winner == "User":
            self.user_coins += self.pot
        elif winner == "Computer":
            self.computer_coins += self.pot
        self.pot = 0  # Reset the pot
