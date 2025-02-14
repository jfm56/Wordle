# **Wordle Game** 🎮🔠 

# ** Description**
This **Wordle-style game** challenges players to guess a **random five-letter word** within **six attempts**.  
It includes built-in feedback using **emoji indicators** to guide players:  
✅ **Correct letter & correct position** → `✅`  
✅ **Correct letter but wrong position** → `❓`  
✅ **Incorrect letter** → `❌`  


I implemented this using a combination of **static, class, and instance methods** for efficient handling of calculations and history.

To ensure accuracy and reliability, the calculator is **thoroughly tested** using:
- ✅ **Pytest** (unit testing)
- ✅ **Pylint** (code quality/linting)
- ✅ **Coverage (cov)** (test coverage measurement)

---

## **📌 Setup & Installation**
### **Step 1️⃣: Clone the Repository**
```bash
git clone https://github.com/jfm56/Wordle.git
cd Wordle

### **Step 2️⃣: Create a Virtual Environment**
bash
python -m venv venv


### **Step 3️⃣: Activate the Virtual Environment**
- **Mac/Linux:**
  
bash
  source venv/bin/activate

- **Windows (Command Prompt):**
  
bash
  venv\Scripts\activate

- **Windows (PowerShell):**
  
powershell
  venv\Scripts\Activate.ps1


### **Step 4️⃣: Install Dependencies**
bash
pip install -r requirements.txt


---

## **📌 Running Tests**
To ensure wordle functions correctly, run:
bash
pytest --pylint --cov


- ✅ **Pytest** runs unit tests.
- ✅ **Pylint** checks for code style issues.
- ✅ **Coverage (cov)** measures test coverage.

# **🛠 How to Play?**
bash
python wordle.py
Gameplay Instructions: 1️⃣ Enter a five-letter word when prompted.
2️⃣ Receive emoji-based feedback (✅ ❓ ❌).
3️⃣ You have six attempts to guess the correct word.
4️⃣ If correct → You win! 🎉
5️⃣ If out of attempts → The correct word is revealed.

--

#**Example Gameplay**

🎮 Welcome to Wordle! You have 6 attempts to guess a five-letter word.

Attempt 1: Enter a five-letter word: apple  
Feedback: ✅❌❌❌❌  

Attempt 2: Enter a five-letter word: happy  
🎉 Congratulations! You guessed the word correctly.

#**📜 Code Structure**
bash
Wordle/
│── wordle.py        # Main game logic
│── __init__.py      # Module initialization
│── README.md        # Project documentation
│── requirements.txt # Dependencies
