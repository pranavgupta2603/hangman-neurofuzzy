import streamlit as st
import random
from display_hangman import display_hangman
from llmthing import get_def

def choose_word():
    words = ["python", "jupyter", "algorithm", "function", "variable", "exception", "dictionary"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman_game():
    # Using session state to persist state between sidebar actions
    if 'word' not in st.session_state:
        st.session_state['word'] = choose_word()
        st.session_state['guessed_letters'] = set()
        st.session_state['attempts_remaining'] = 7
        st.session_state['correct_guesses'] = set(st.session_state['word'])

    word = st.session_state['word']
    guessed_letters = st.session_state['guessed_letters']
    attempts_remaining = st.session_state['attempts_remaining']
    correct_guesses = st.session_state['correct_guesses']

    st.title("Hangman Game")
    st.write("Guess the word. You have 7 attempts to guess wrong letters.")
    lol = display_hangman(attempts_remaining-1)
    st.code(lol)

    if attempts_remaining > 0 and correct_guesses:
        st.write("Word: ", display_word(word, guessed_letters))
        st.write(f"Attempts remaining: {attempts_remaining}")
        
        guess = st.text_input("Guess a letter:", key="new_guess")

        if st.button("Guess"):
            if len(guess) == 1 and guess.isalpha():
                guess = guess.lower()
                if guess in guessed_letters:
                    st.warning("You have already guessed that letter.")
                else:
                    guessed_letters.add(guess)
                    if guess in correct_guesses:
                        correct_guesses.remove(guess)
                        st.success("Good guess!")
                    else:
                        attempts_remaining -= 1
                        st.error("Sorry, that letter is not in the word.")
                    st.session_state['attempts_remaining'] = attempts_remaining
            else:
                st.error("Please enter a single alphabetic character.")

    if not correct_guesses:
        st.success(f"Congratulations! You've guessed the word: {word}")
        st.success(f"Definition: {get_def(word)}")
    elif attempts_remaining <= 0:
        st.error(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman_game()
