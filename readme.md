Wordle Game 🎮🔠

A simple Wordle-style game built in Python that allows players to guess a random five-letter word with up to six attempts. Players receive feedback on their guesses using emojis ✅ ❌ ❓ to indicate correct, incorrect, or misplaced letters.
📌 Features

✅ Random word selection – The game picks a random five-letter word from a predefined list.
✅ Guess validation – Ensures players enter exactly five letters.
✅ Feedback system – Uses ✅ (correct letter & position), ❓ (correct letter, wrong position), and ❌ (incorrect letter).
✅ Game loop – Players have six attempts to guess the word.
✅ Easy-to-run – Works in the terminal with a simple Python script.
🚀 Installation & Setup

🔹 Clone the Repository
git clone https://github.com/jfm56/Wordle.git
cd Wordle
🔹 Create a Virtual Environment (Optional, but Recommended)
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
🔹 Install Dependencies (if any in the future)
pip install -r requirements.txt
(Note: No dependencies required for the current version.)
🛠 How to Play?

1️⃣ Run the game:
python wordle.py
2️⃣ Guess the word:
Enter a five-letter word when prompted.
Get emoji-based feedback on your guess.
3️⃣ Winning or Losing:
If you guess correctly, you win! 🎉
If you run out of attempts, the correct word is revealed.
📌 Example Gameplay

🎮 Welcome to Wordle! You have 6 attempts to guess a five-letter word.

Attempt 1: Enter a five-letter word: apple  
Feedback: ✅❌❌❌❌  

Attempt 2: Enter a five-letter word: puppy  
🎉 Congratulations! You guessed the word correctly.
📜 Code Structure

wordle.py → Main game logic
__init__.py → Module initialization
README.md → This documentation
🧪 Running Tests (if applicable in future versions)

pytest --pylint --cov
🤝 Contributing

Feel free to fork this repository and submit pull requests to improve the game! 🚀
