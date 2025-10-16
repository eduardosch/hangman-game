# 🎮 Hangman Game

A colorful terminal-based Hangman game with scoring system, high score leaderboard, and sound effects!

## 🚀 Quick Start

### 1. Clone or Download

```bash
git clone git@github.com:eduardosch/hangman-game.git
cd hangman-game
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows (Git Bash/WSL):**

```bash
source venv/Scripts/activate
```

**Windows (CMD):**

```cmd
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Game!

```bash
python hangman.py
```

## 📁 Project Structure

```
hangman-game/
├── hangman.py          # Main game file
├── requirements.txt    # Python dependencies
├── highscores.json     # High scores (auto-generated)
├── words/              # Word lists by difficulty
│   ├── easy.json
│   ├── medium.json
│   └── hard.json
└── sounds/             # Optional sound effects
    ├── correct.wav
    ├── wrong.wav
    ├── win.wav
    └── lose.wav
```

## 🎯 Features

- ✅ 3 difficulty levels (Easy, Medium, Hard)
- ✅ 234 words across various categories
- ✅ Colorful terminal interface
- ✅ Score system with leaderboard
- ✅ Sound effects support
- ✅ High score tracking
- ✅ Real-time feedback

## 🎨 Dependencies

- **colorama** (0.4.6): Terminal colors
- **playsound** (1.2.2): Sound effects

## 📝 Requirements

- Python 3.7 or higher
- pip (Python package manager)

## 🎮 How to Play

1. Choose difficulty level (1-3) or view high scores (4)
2. Guess letters one at a time
3. Complete the word before 6 wrong guesses
4. Higher scores for fewer mistakes!
5. Enter your name to save your score

## 🏆 Scoring System

- **Base Score**: Word length × 10
- **Difficulty Multiplier**: Easy (×1), Medium (×1.5), Hard (×2)
- **Penalty**: -5 points per wrong guess

## 🤝 Contributing

Feel free to add more words to the JSON files or suggest new features!

## 📄 License

MIT License - Feel free to use and modify!

## 👨‍💻 Author

Eduardo Schröder - [https://github.com/eduardosch]

---

**Happy Gaming! 🎉**
