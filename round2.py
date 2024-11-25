# import random

# def play_round(self):
#     """Play a single round of the game."""
#     print("\n--- New Round ---")
#     self.deal.show_balances()

#     # Betting phase
#     user_bet = int(input("\nEnter your bet amount: "))
#     if user_bet > self.deal.user_coins:
#         print("You don't have enough coins to place this bet.")
#         return False

#     if not self.deal.place_bet("User", user_bet):
#         print("Bet placement failed. Exiting round.")
#         return False

#     computer_bet = min(user_bet, self.deal.computer_coins)
#     self.deal.place_bet("Computer", computer_bet)

#     print("\nBoth players have placed their bets!")
#     self.deal_cards()

#     user = self.players[0]
#     computer = self.players[1]

#     while True:
#         print("\nOptions:")
#         print("1. Show my cards")
#         print("2. Reveal winner (show computer's cards)")
#         print("3. Add to the bet (up to 500 coins)")
#         print("4. Exit game")

#         # User's turn to choose
#         user_choice = input("Enter your choice (1/2/3/4): ")

#         if user_choice == '1':
#             print(f"\n{user.name}'s cards:")
#             user.display_hand()
#         elif user_choice == '2':
#             print(f"\n{computer.name}'s cards:")
#             computer.display_hand()
#             winner = self.find_winner()
#             winner_name = winner[1]
#             print(f"\nThe winner is {winner_name}!")

#             # Update coin balances
#             if winner_name == user.name:
#                 self.deal.distribute_winnings("User")
#             else:
#                 self.deal.distribute_winnings("Computer")
#             break
#         elif user_choice == '3':
#             additional_bet = random.randint(1, 500)
#             if self.deal.user_coins >= additional_bet:
#                 self.deal.place_bet("User", additional_bet)
#                 print(f"\nYou added {additional_bet} coins to the bet.")
#             else:
#                 print("\nYou don't have enough coins to add to the bet.")
#         elif user_choice == '4':
#             print("Exiting the game. Goodbye!")
#             return True
#         else:
#             print("Invalid choice. Please try again.")

#         # Computer's turn to choose (randomly selects 2, 3, or 4)
#         computer_choice = random.choice(['2', '3', '4'])

#         if computer_choice == '2':
#             print(f"\n{computer.name} chooses to reveal the winner!")
#             print(f"\n{computer.name}'s cards:")
#             computer.display_hand()
#             winner = self.find_winner()
#             winner_name = winner[1]
#             print(f"\nThe winner is {winner_name}!")

#             # Update coin balances
#             if winner_name == user.name:
#                 self.deal.distribute_winnings("User")
#             else:
#                 self.deal.distribute_winnings("Computer")
#             break
#         elif computer_choice == '3':
#             additional_bet = random.randint(1, 500)
#             if self.deal.computer_coins >= additional_bet:
#                 self.deal.place_bet("Computer", additional_bet)
#                 print(f"\n{computer.name} added {additional_bet} coins to the bet.")
#             else:
#                 print(f"\n{computer.name} doesn't have enough coins to add to the bet.")
#         elif computer_choice == '4':
#             print(f"\n{computer.name} chooses to exit the game. Goodbye!")
#             return True

#     self.deal.show_balances()
#     return False  # Round finished, continue playing
