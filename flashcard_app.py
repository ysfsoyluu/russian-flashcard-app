# Flashcard App — Russian / English
# Author: Yusuf Soylu
# Study Russian vocabulary with score tracking and multiple study modes

import random

# ============================================================
#  FLASHCARD DECK — Add as many word pairs as you like!
# ============================================================

flashcards = [
    {"russian": "привет",       "english": "hello"},
    {"russian": "пока",         "english": "goodbye"},
    {"russian": "спасибо",      "english": "thank you"},
    {"russian": "пожалуйста",   "english": "please / you're welcome"},
    {"russian": "да",           "english": "yes"},
    {"russian": "нет",          "english": "no"},
    {"russian": "дом",          "english": "house"},
    {"russian": "вода",         "english": "water"},
    {"russian": "еда",          "english": "food"},
    {"russian": "книга",        "english": "book"},
    {"russian": "работа",       "english": "work"},
    {"russian": "время",        "english": "time"},
    {"russian": "друг",         "english": "friend"},
    {"russian": "город",        "english": "city"},
    {"russian": "машина",       "english": "car"},
    {"russian": "деньги",       "english": "money"},
    {"russian": "язык",         "english": "language"},
    {"russian": "учиться",      "english": "to study"},
    {"russian": "говорить",     "english": "to speak"},
    {"russian": "понимать",     "english": "to understand"},
]


# ============================================================
#  HELPER FUNCTIONS
# ============================================================

def show_score(correct, total):
    if total == 0:
        return
    percentage = (correct / total) * 100
    print(f"\n{'='*40}")
    print(f"  📊 Your Score: {correct}/{total}  ({percentage:.1f}%)")
    if percentage == 100:
        print("  🏆 Perfect score! Excellent work!")
    elif percentage >= 80:
        print("  🌟 Great job! Keep it up!")
    elif percentage >= 50:
        print("  💪 Good effort! Keep practicing.")
    else:
        print("  📚 Keep studying — you'll get there!")
    print(f"{'='*40}")


def normalize(text):
    """Make comparison case-insensitive and strip extra spaces."""
    return text.strip().lower()


# ============================================================
#  MODE 1 — STUDY MODE (flip through all cards)
# ============================================================

def study_mode():
    print("\n📖 STUDY MODE — Flip through all cards")
    print("Press Enter to reveal the answer. Type 'q' to quit.\n")

    deck = flashcards.copy()
    random.shuffle(deck)

    for i, card in enumerate(deck, start=1):
        print(f"Card {i}/{len(deck)}")
        print(f"  🇷🇺  {card['russian']}")
        user = input("  Press Enter to see the English translation... ")
        if user.strip().lower() == "q":
            print("Exiting study mode.")
            return
        print(f"  🇬🇧  {card['english']}\n")

    print("✅ You've gone through all the cards!")


# ============================================================
#  MODE 2 — QUIZ MODE (Russian → type English answer)
# ============================================================

def quiz_mode():
    print("\n✏️  QUIZ MODE — Translate Russian to English")
    print("Type your answer and press Enter. Type 'q' to quit.\n")

    deck = flashcards.copy()
    random.shuffle(deck)

    correct = 0
    total = 0

    for i, card in enumerate(deck, start=1):
        print(f"Question {i}/{len(deck)}")
        print(f"  🇷🇺  {card['russian']}")
        answer = input("  Your answer: ")

        if normalize(answer) == "q":
            print("Exiting quiz.")
            break

        total += 1
        correct_answers = [a.strip().lower() for a in card["english"].split("/")]

        if normalize(answer) in correct_answers:
            print("  ✅ Correct!\n")
            correct += 1
        else:
            print(f"  ❌ Incorrect. The answer is: {card['english']}\n")

    show_score(correct, total)


# ============================================================
#  MODE 3 — REVERSE QUIZ (English → type Russian answer)
# ============================================================

def reverse_quiz_mode():
    print("\n🔄 REVERSE QUIZ — Translate English to Russian")
    print("Type your answer in Russian. Type 'q' to quit.\n")

    deck = flashcards.copy()
    random.shuffle(deck)

    correct = 0
    total = 0

    for i, card in enumerate(deck, start=1):
        print(f"Question {i}/{len(deck)}")
        print(f"  🇬🇧  {card['english']}")
        answer = input("  Your answer (in Russian): ")

        if normalize(answer) == "q":
            print("Exiting quiz.")
            break

        total += 1

        if normalize(answer) == normalize(card["russian"]):
            print("  ✅ Correct!\n")
            correct += 1
        else:
            print(f"  ❌ Incorrect. The answer is: {card['russian']}\n")

    show_score(correct, total)


# ============================================================
#  MODE 4 — RANDOM CARD (quick single card practice)
# ============================================================

def random_card_mode():
    print("\n🎲 RANDOM CARD MODE — Quick practice")
    print("Press Enter for a new card. Type 'q' to quit.\n")

    while True:
        card = random.choice(flashcards)
        direction = random.choice(["ru_to_en", "en_to_ru"])

        if direction == "ru_to_en":
            print(f"  🇷🇺  {card['russian']}")
            user = input("  Press Enter to see translation... ")
            if normalize(user) == "q":
                break
            print(f"  🇬🇧  {card['english']}\n")
        else:
            print(f"  🇬🇧  {card['english']}")
            user = input("  Press Enter to see translation... ")
            if normalize(user) == "q":
                break
            print(f"  🇷🇺  {card['russian']}\n")

    print("Exiting random card mode.")


# ============================================================
#  MAIN MENU
# ============================================================

def main():
    print("╔══════════════════════════════════════╗")
    print("║      🇷🇺  Russian Flashcard App  🇬🇧   ║")
    print("╚══════════════════════════════════════╝")
    print(f"  {len(flashcards)} cards loaded\n")

    while True:
        print("Choose a study mode:")
        print("  1 — 📖 Study Mode       (flip through all cards)")
        print("  2 — ✏️  Quiz Mode        (Russian → English)")
        print("  3 — 🔄 Reverse Quiz     (English → Russian)")
        print("  4 — 🎲 Random Card      (quick single card practice)")
        print("  5 — 🚪 Quit")
        print("--------------------------------------")

        choice = input("Your choice (1/2/3/4/5): ")

        if choice == "1":
            study_mode()
        elif choice == "2":
            quiz_mode()
        elif choice == "3":
            reverse_quiz_mode()
        elif choice == "4":
            random_card_mode()
        elif choice == "5":
            print("\nДо свидания! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


main()
