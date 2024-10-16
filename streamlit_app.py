import random

def coin_toss_game():
    balance = 100  # Starting balance
    print("Welcome to the Coin Toss Game!")
    
    while True:
        print(f"Your current balance is: ${balance:.2f}")
        
        # Get user's bet and choice
        bet = input("Enter your bet amount (or type 'q' to quit): ")
        if bet.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break

        try:
            bet = float(bet)
            if bet > balance:
                print("You cannot bet more than your current balance.")
                continue
            if bet <= 0:
                print("Please enter a positive amount.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        choice = input("Choose heads or tails: ").lower()
        if choice not in ['heads', 'tails']:
            print("Invalid choice. Please choose 'heads' or 'tails'.")
            continue

        # Coin toss logic
        outcome = random.choice(['heads', 'tails'])
        print(f"The coin shows: {outcome}")

        # Determine win/loss
        if choice == outcome:
            balance += bet
            print(f"You win! Your new balance is: ${balance:.2f}")
        else:
            balance -= bet
            print(f"You lose! Your new balance is: ${balance:.2f}")

        # Check if player wants to continue
        if balance <= 0:
            print("You have run out of money! Game over.")
            break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

coin_toss_game()

    
