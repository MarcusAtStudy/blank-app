import random

def coin_toss_game():
    balance = 100  # Starting balance
    print("Welcome to the Coin Toss Game!")
    
    while True:
        print(f"Your current balance is: ${balance}")
        
        # Get user's bet and choice
        try:
            bet = float(input("Enter your bet amount (or type 'q' to quit): "))
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

python coin_toss_game.py


    
