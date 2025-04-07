```markdown
# 🎮 Wordle Game (Python Edition)

A command-line Wordle-style game where players guess a secret five-letter word within six attempts. Emoji-based feedback guides players after each guess.

---

## 📦 Features

- ✅ **Emoji Feedback**:
  - ✅ = Correct letter & correct position
  - ❓ = Correct letter but wrong position
  - ❌ = Incorrect letter
- 🧠 Encapsulated logic using a `Wordle` class
- 🧪 Fully tested using **Pytest**
- 📏 Code quality checked using **Pylint**
- 🧪📊 Test coverage tracked with **Coverage.py**

---

## 📁 Project Structure

```
Wordle/
├── Wordle/               # Package directory
│   └── __init__.py       # Contains the Wordle class and game logic
├── play.py               # Entry point to run the game
├── test_Wordle.py        # Unit tests
├── requirements.txt      # Project dependencies
├── .pylintrc             # Pylint config
├── pytest.ini            # Pytest config
├── .coverage             # Test coverage cache
├── README.md             # You're reading it
```

---

## 🧰 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jfm56/Wordle.git
cd Wordle
```

### 2️⃣ Create & Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Game

```bash
python play.py
```

---

## 🧪 Running Tests, Linting & Coverage

```bash
pytest --pylint --cov
```

This will:
- Run your unit tests with Pytest
- Lint your code with Pylint
- Show test coverage with Coverage

---

## 🎮 How to Play

- Enter a five-letter word when prompted.
- Get feedback using emoji:
  - ✅: correct letter & position
  - ❓: correct letter, wrong position
  - ❌: incorrect letter
- Guess the word within 6 tries.

---

## 🧑‍💻 Author

Made with ❤️ by [jfm56](https://github.com/jfm56)

---

```