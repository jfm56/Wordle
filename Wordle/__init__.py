'''Operations to create a five letter word, and check guessing.'''
import random

class Wordle:
    """Generates word, chesks guess, and preforms main loop"""
    @staticmethod
    def generate_word():
        """Generate a five letter word."""
        return "puppy"

    @staticmethod
    def check_guess(secret_word, guess):
        """Check the guessed word and provide feedback."""
        feedback_symbols = [("✅" * (g == s)) +
                        ("❓" * (g in secret_word and g !=s)) +
                        ("❌" * (g not in secret_word))
                        for g, s in zip(guess, secret_word)
    ]
        return "".join(feedback_symbols)
