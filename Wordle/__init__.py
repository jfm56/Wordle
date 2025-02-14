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

    @staticmethod
    def wordle():
        """Main game loop"""
        secret_word = Wordle.generate_word()
        attempts = 6

        print("Welcome to Wordle! You have 6 attempts to guess a five-letter word.")

        for attempt in range(1, attempts + 1):
            guess = input (f"Attempt {attempt}: Enter a five-letter word: ").lower()

            if len(guess) != 5:
                print("Invalad input. please enter exactly five letters.")
                continue

            print ("Feedback:", Wordle.check_guess(secret_word, guess))

            if guess == secret_word:
                print("Congratulations! You guessed the word corresctly.")
                return

        print (f"Game over! The correct word was: {secret_word}")

    if __name__ == "__main__":
        wordle()
