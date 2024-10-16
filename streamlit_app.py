pip install streamlit

import streamlit as st
import random

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 100  # Starting balance

st.title("Coin Toss Gambling Game")
st.write(f"Your current balance is: ${st.session_state.balance:.2f}")

# User input for bet
bet = st.number_input("Enter your bet amount (max $100):", min_value=0.0, max_value=st.session_state.balance, step=1.0)

# User choice
choice = st.selectbox("Choose heads or tails:", ["heads", "tails"])

if st.button("Toss Coin"):
    if bet > 0:
        # Coin toss logic
        outcome = random.choice(['heads', 'tails'])
        st.write(f"The coin shows: {outcome}")

        # Determine win/loss
        if choice == outcome:
            st.session_state.balance += bet
            st.success(f"You win! Your new balance is: ${st.session_state.balance:.2f}")
        else:
            st.session_state.balance -= bet
            st.error(f"You lose! Your new balance is: ${st.session_state.balance:.2f}")
    else:
        st.warning("Please enter a valid bet amount.")

# Check if the balance is zero
if st.session_state.balance <= 0:
    st.error("You have run out of money! Game over.")
    st.session_state.balance = 100  # Reset the balance

streamlit run app.py
