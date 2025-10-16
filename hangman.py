import random
import os
import json
from datetime import datetime

# Try to import colorama for colors
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    print("Colorama not installed. Run: pip install colorama")

# Try to import playsound for sound effects
try:
    from playsound import playsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    print("Playsound not installed. Run: pip install playsound")

# ASCII hangman drawings
HANGMAN_PICS = [
    """
       ______
       |    |
       |
       |
       |
       |
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |
       |
       |
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |    |
       |
       |
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|
       |
       |
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|\\
       |
       |
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|\\
       |   /
       |
    ___|___
    """,
    """
       ______
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ___|___
    """
]

SCORES_FILE = "highscores.json"

def color_text(text, color="white"):
    """Returns colored text if colorama is available"""
    if not COLORS_AVAILABLE:
        return text
    
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "bright_green": Fore.GREEN + Style.BRIGHT,
        "bright_red": Fore.RED + Style.BRIGHT,
        "bright_yellow": Fore.YELLOW + Style.BRIGHT
    }
    return colors.get(color, "") + text + Style.RESET_ALL

def play_sound(sound_type):
    """Plays sound effects (placeholder for now)"""
    if not SOUND_AVAILABLE:
        return
    
    # You can add sound files later
    sounds = {
        "correct": "sounds/correct.wav",
        "wrong": "sounds/wrong.wav",
        "win": "sounds/win.wav",
        "lose": "sounds/lose.wav"
    }
    
    if sound_type in sounds and os.path.exists(sounds[sound_type]):
        playsound(sounds[sound_type], block=False)
    pass

def load_words(difficulty):
    """Loads words from JSON file based on difficulty"""
    filename = f"words/{difficulty}.json"
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = json.load(file)
            return words
    except FileNotFoundError:
        print(color_text(f"\n❌ Error: '{filename}' not found!", "red"))
        print(f"Make sure you have {filename} in the correct folder.")
        input("\nPress Enter to exit...")
        exit()
    except json.JSONDecodeError:
        print(color_text(f"\n❌ Error: '{filename}' is not a valid JSON file!", "red"))
        input("\nPress Enter to exit...")
        exit()

def load_highscores():
    """Loads high scores from file"""
    if not os.path.exists(SCORES_FILE):
        return []
    
    try:
        with open(SCORES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []

def save_highscore(player_name, score, difficulty):
    """Saves a new high score"""
    scores = load_highscores()
    
    scores.append({
        "name": player_name,
        "score": score,
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    
    # Keep only top 10 scores
    scores.sort(key=lambda x: x["score"], reverse=True)
    scores = scores[:10]
    
    with open(SCORES_FILE, 'w', encoding='utf-8') as file:
        json.dump(scores, file, indent=4)

def show_highscores():
    """Displays the high scores leaderboard"""
    scores = load_highscores()
    
    if not scores:
        print(color_text("\n📊 No high scores yet! Be the first!", "yellow"))
        return
    
    print(color_text("\n" + "=" * 60, "cyan"))
    print(color_text("                    🏆 HIGH SCORES 🏆", "bright_yellow"))
    print(color_text("=" * 60, "cyan"))
    print(f"{'Rank':<6} {'Name':<15} {'Score':<10} {'Difficulty':<12} {'Date':<15}")
    print(color_text("-" * 60, "cyan"))
    
    for i, score in enumerate(scores, 1):
        rank_color = "bright_yellow" if i == 1 else "yellow" if i <= 3 else "white"
        print(f"{color_text(f'{i}.', rank_color):<12} {score['name']:<15} {color_text(str(score['score']), 'green'):<18} {score['difficulty']:<12} {score['date']:<15}")
    
    print(color_text("=" * 60 + "\n", "cyan"))

def calculate_score(word_length, errors, difficulty):
    """Calculates the final score based on performance"""
    base_score = word_length * 10
    difficulty_multiplier = {"easy": 1, "medium": 1.5, "hard": 2}
    penalty = errors * 5
    
    score = int((base_score * difficulty_multiplier[difficulty]) - penalty)
    return max(score, 0)

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_difficulty():
    """Allows the player to choose difficulty level"""
    print(color_text("=" * 50, "cyan"))
    print(color_text("         WELCOME TO HANGMAN GAME!", "bright_yellow"))
    print(color_text("=" * 50, "cyan"))
    print("\nChoose difficulty level:")
    print(f"{color_text('1', 'green')} - Easy (3-6 letter words)")
    print(f"{color_text('2', 'yellow')} - Medium (6-9 letter words)")
    print(f"{color_text('3', 'red')} - Hard (9+ letter words)")
    print(f"{color_text('4', 'cyan')} - View High Scores")
    
    while True:
        choice = input(f"\n{color_text('Enter 1, 2, 3, or 4:', 'magenta')} ").strip()
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        elif choice == '4':
            show_highscores()
            input(color_text("\nPress Enter to continue...", "cyan"))
            clear_screen()
            return choose_difficulty()
        else:
            print(color_text("Invalid option! Try again.", "red"))

def display_game(hidden_word, errors, wrong_letters, hint, score, last_guess=None, was_correct=None):
    """Displays the current game state"""
    clear_screen()
    print(color_text("=" * 50, "cyan"))
    print(color_text("                HANGMAN GAME", "bright_yellow"))
    print(color_text("=" * 50, "cyan"))
    
    # Hangman drawing with color
    hangman_color = "red" if errors >= 4 else "yellow" if errors >= 2 else "white"
    print(color_text(HANGMAN_PICS[errors], hangman_color))
    
    print(f"\n{color_text('Hint:', 'cyan')} {hint}")
    print(f"\n{color_text('Word:', 'bright_yellow')} {' '.join(hidden_word)}")
    
    # Show feedback for last guess
    if last_guess:
        if was_correct:
            print(f"\n{color_text('✓ Correct!', 'bright_green')} Letter '{last_guess}' is in the word!")
        else:
            print(f"\n{color_text('✗ Wrong!', 'bright_red')} Letter '{last_guess}' is not in the word.")
    
    print(f"\n{color_text('Wrong letters:', 'red')} {', '.join(sorted(wrong_letters)) if wrong_letters else 'None'}")
    print(f"{color_text('Attempts remaining:', 'green')} {color_text(str(6 - errors), 'bright_green')}")
    print(f"{color_text('Current Score:', 'magenta')} {color_text(str(score), 'bright_yellow')}")
    print(color_text("=" * 50, "cyan"))

def play():
    """Main game function"""
    difficulty = choose_difficulty()
    words = load_words(difficulty)
    item = random.choice(words)
    word = item['word'].upper()
    hint = item['hint']
    
    hidden_word = ['_'] * len(word)
    used_letters = set()
    wrong_letters = set()
    errors = 0
    max_errors = 6
    last_guess = None
    was_correct = None
    
    while errors < max_errors and '_' in hidden_word:
        current_score = calculate_score(len(word), errors, difficulty)
        display_game(hidden_word, errors, wrong_letters, hint, current_score, last_guess, was_correct)
        
        # Get letter from player
        letter = input(f"\n{color_text('Enter a letter:', 'cyan')} ").upper().strip()
        
        # Validations
        if len(letter) != 1:
            last_guess = letter
            was_correct = None
            continue
        
        if not letter.isalpha():
            last_guess = None
            was_correct = None
            continue
        
        if letter in used_letters:
            last_guess = None
            was_correct = None
            continue
        
        used_letters.add(letter)
        last_guess = letter
        
        # Check if letter is in the word
        if letter in word:
            play_sound("correct")
            was_correct = True
            for i, char in enumerate(word):
                if char == letter:
                    hidden_word[i] = letter
        else:
            play_sound("wrong")
            was_correct = False
            wrong_letters.add(letter)
            errors += 1
    
    # End of game
    final_score = calculate_score(len(word), errors, difficulty)
    display_game(hidden_word, errors, wrong_letters, hint, final_score)
    
    if '_' not in hidden_word:
        print(color_text("\n🎉 CONGRATULATIONS! You won! 🎉", "bright_green"))
        print(color_text(f"Final Score: {final_score}", "bright_yellow"))
        play_sound("win")
        
        # Save high score
        player_name = input(color_text("\nEnter your name for the leaderboard: ", "cyan")).strip()
        if player_name:
            save_highscore(player_name, final_score, difficulty)
            print(color_text("Score saved!", "green"))
    else:
        print(color_text(f"\n💀 GAME OVER! The word was: {word}", "bright_red"))
        print(color_text(f"Final Score: {final_score}", "yellow"))
        play_sound("lose")
    
    print(color_text("\n" + "=" * 50, "cyan"))

def main():
    """Main function with restart loop"""
    while True:
        play()
        
        answer = input(f"\n{color_text('Do you want to play again? (y/n):', 'cyan')} ").lower().strip()
        if answer != 'y':
            clear_screen()
            show_highscores()
            print(color_text("=" * 50, "cyan"))
            print(color_text("     Thanks for playing! See you next time! 👋", "bright_yellow"))
            print(color_text("=" * 50 + "\n", "cyan"))
            break

if __name__ == "__main__":
    main()