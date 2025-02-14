# Wordle Game 🎮🔠

## **Description**
This Wordle-style game challenges players to guess a random five-letter word within six attempts.
It includes built-in feedback using emoji indicators to guide players:

- ✅ Correct letter & correct position → ✅
- ✅ Correct letter but wrong position → ❓
- ✅ Incorrect letter → ❌

The implementation utilizes a combination of static, class, and instance methods for efficient handling of calculations and history.

To ensure accuracy and reliability, the game is thoroughly tested using:

- ✅ **Pytest** (unit testing)
- ✅ **Pylint** (code quality/linting)
- ✅ **Coverage (cov)** (test coverage measurement)

---

## **📌 Setup & Installation**

### **Step 1️⃣: Clone the Repository**
```sh
git clone https://github.com/jfm56/Wordle.git
cd Wordle
```

### **Step 2️⃣: Create a Virtual Environment**
```sh
python -m venv venv
```

### **Step 3️⃣: Activate the Virtual Environment**
- **Mac/Linux:**  
  ```sh
  source venv/bin/activate
  ```
- **Windows (Command Prompt):**  
  ```sh
  venv\Scripts\activate
  ```
- **Windows (PowerShell):**  
  ```powershell
  venv\Scripts\Activate.ps1
  ```

### **Step 4️⃣: Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **📌 Running Tests**
To ensure the Wordle game functions correctly, run:
```sh
pytest --pylint --cov
```

- ✅ **Pytest** runs unit tests.
- ✅ **Pylint** checks for code style issues.
- ✅ **Coverage (cov)** measures test coverage.

---

## **🛠 How to Play?**
Run the game using:
```sh
python wordle.py
```

### **Gameplay Instructions**  
1️⃣ Enter a five-letter word when prompted.  
2️⃣ Receive emoji-based feedback (✅ ❓ ❌).  
3️⃣ You have six attempts to guess the correct word.  
4️⃣ If correct → You win! 🎉  
5️⃣ If out of attempts → The correct word is revealed.  

---

## **🎯 Example Gameplay**
```
🎮 Welcome to Wordle! You have 6 attempts to guess a five-letter word.

Attempt 1: Enter a five-letter word: apple  
Feedback: ✅❌❌❌❌  

Attempt 2: Enter a five-letter word: happy  
🎉 Congratulations! You guessed the word correctly.
```

---

## **📜 Code Structure**
```
Wordle/
│── wordle.py        # Main game logic
│── __init__.py      # Module initialization
│── README.md        # Project documentation
│── requirements.txt # Dependencies
```

