from deck import Deck
from player import Player
from deal import Deal
from card import Card
import random

class TeenPattiGame:
    def __init__(self, player_names):
        self.mydeck = Deck()
        self.players = [Player(name) for name in player_names]
        self.deal = Deal()  # Initialize betting system

    def deal_cards(self):
        """Distribute cards to players."""
        for player in self.players:
            player.receive_cards([self.mydeck.deal() for _ in range(3)])

    def evaluate_hand(self, hand):
        """Evaluate the hand to determine its score."""
        ranks = [card.rank for card in hand]
        suits = [card.suit for card in hand]

        rank_values = [Card.ranks.index(rank) for rank in ranks]
        rank_values.sort()

        if len(set(ranks)) == 1:  # Trail/Set/Trio
            return (5, rank_values[-1])
        if len(set(suits)) == 1 and rank_values[2] - rank_values[0] == 2:  # Pure Sequence
            return (4, rank_values[-1])
        if rank_values[2] - rank_values[0] == 2:  # Sequence
            return (3, rank_values[-1])
        if len(set(suits)) == 1:  # Color/Flush
            return (2, rank_values[-1])
        if len(set(ranks)) == 2:  # Pair
            pair_value = max(rank_values, key=rank_values.count)
            return (1, pair_value)
        return (0, rank_values[-1])  # High Card
    
    
    def find_winner(self):
        """Find the winner based on hand evaluations."""
        scores = [(self.evaluate_hand(player.hand), player.name) for player in self.players]
        winner = max(scores, key=lambda x: x[0])  # Find the player with the highest score
        return winner  # Return the winner's score and name


    
    def play_round(self):
        """Play a single round of the game."""
        print("\n--- New Round ---")
        self.deal.show_balances()

        # Betting phase
        user_bet = int(input("\nEnter your bet amount: "))
        if user_bet > self.deal.user_coins:
            print("You don't have enough coins to place this bet.")
            return False

        if not self.deal.place_bet("User", user_bet):
            print("Bet placement failed. Exiting round.")
            return False

        computer_bet = min(user_bet, self.deal.computer_coins)
        self.deal.place_bet("Computer", computer_bet)

        print("\nBoth players have placed their bets!")
        self.deal_cards()

        user = self.players[0]
        computer = self.players[1]

        while True:
            print("\nOptions:")
            print("1. Show my cards")
            print("2. Reveal winner (show computer's cards)")
            print("3. Add to the bet (up to 500 coins)")
            print("4. Exit game")
            print("5. Computer choice (add coins or reveal winner)")

            # User's turn to choose
            user_choice = input("Enter your choice (1/2/3/4/5): ")

            if user_choice == '1':
                print(f"\n{user.name}'s cards:")
                user.display_hand()
            elif user_choice == '2':
                print(f"\n{computer.name}'s cards:")
                computer.display_hand()
                winner = self.find_winner()
                winner_name = winner[1]
                print(f"\nThe winner is {winner_name}!")

                # Update coin balances
                if winner_name == user.name:
                    self.deal.distribute_winnings("User")
                else:
                    self.deal.distribute_winnings("Computer")
                break
            elif user_choice == '3':
                try:
                    additional_bet = int(input("\nEnter the amount you want to add to the bet (up to 500 coins): "))
                    if additional_bet > 500:
                        print("You cannot add more than 500 coins at once. Try again.")
                    elif self.deal.user_coins >= additional_bet:
                        self.deal.place_bet("User", additional_bet)
                        print(f"\nYou added {additional_bet} coins to the bet.")
                    else:
                        print("\nYou don't have enough coins to add to the bet.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif user_choice == '4':
                print("Exiting the game. Goodbye!")
                return True
            elif user_choice == '5':
                # Computer's dynamic choice
                computer_choice = random.choices(['add_coins', 'reveal_winner'], weights=[80, 20], k=1)[0]

                if computer_choice == 'add_coins':
                    additional_bet = random.randint(1, 500)
                    if self.deal.computer_coins >= additional_bet:
                        self.deal.place_bet("Computer", additional_bet)
                        print(f"\n{computer.name} added {additional_bet} coins to the bet.")
                    else:
                        print(f"\n{computer.name} doesn't have enough coins to add to the bet.")
                elif computer_choice == 'reveal_winner':
                    print(f"\n{computer.name} chooses to reveal the winner!")
                    print(f"\n{computer.name}'s cards:")
                    computer.display_hand()
                    winner = self.find_winner()
                    winner_name = winner[1]
                    print(f"\nThe winner is {winner_name}!")

                    # Update coin balances
                    if winner_name == user.name:
                        self.deal.distribute_winnings("User")
                    else:
                        self.deal.distribute_winnings("Computer")
                    break
            else:
                print("Invalid choice. Please try again.")

            self.deal.show_balances()

        return False  # Round finished, continue playing




    def play(self):
        """Start and manage the game until a player exits or runs out of coins."""
        print("\n--- Aaa jao Teen Patti Game Khelian or Sekkhian ! ---")

        while True:
            if self.deal.user_coins <= 0:
                print("\nYou have run out of coins. Game over!")
                break
            if self.deal.computer_coins <= 0:
                print("\nThe computer has run out of coins. You win the game!")
                break

            exit_game = self.play_round()
            if exit_game:
                break

        print("\nFinal Balances:")
        self.deal.show_balances()
        print("\nThanks for playing Teen Patti!")
