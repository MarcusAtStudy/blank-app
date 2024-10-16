import streamlit as st
import random

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 100  # Starting balance
if 'jackpot' not in st.session_state:
    st.session_state.jackpot = 1000  # Jackpot amount

# Define the symbols for the slot machine
symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "⭐", "💰"]

# Function to spin the slot machine
def spin_slots():
    return random.choices(symbols, k=3)

# Streamlit app layout
st.title("Slot Machine Game")
st.write(f"Your current balance is: ${st.session_state.balance:.2f}")

# User input for bet
bet = st.number_input("Enter your bet amount (max $100):", min_value=0.0, max_value=st.session_state.balance, step=1.0)

if st.button("Spin!"):
    if bet > 0:
        # Spin the slot machine
        result = spin_slots()
        st.write(f"🎰 Slots: {result[0]} | {result[1]} | {result[2]} 🎰")

        # Check for win
        if result[0] == result[1] == result[2]:  # All three symbols match
            winnings = bet * 10  # Example winnings multiplier
            st.session_state.balance += winnings
            st.success(f"You win! You received ${winnings:.2f}. Your new balance is: ${st.session_state.balance:.2f}")
        else:
            st.session_state.balance -= bet
            st.error(f"You lose! Your new balance is: ${st.session_state.balance:.2f}")
    else:
        st.warning("Please enter a valid bet amount.")

# Check if the balance is zero
if st.session_state.balance <= 0:
    st.error("You have run out of money! Game over.")
    st.session_state.balance = 100  # Reset the balance


