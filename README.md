[README.md](https://github.com/user-attachments/files/26634322/README.md)
# Russian Flashcard App

A Python terminal app for studying Russian vocabulary with four different study modes and score tracking.

## Features

- **20 Russian/English word pairs** built in — easily expandable
- **4 study modes:**
  - 📖 Study Mode — flip through all cards at your own pace
  - ✏️ Quiz Mode — translate Russian → English, get scored
  - 🔄 Reverse Quiz — translate English → Russian
  - 🎲 Random Card — quick single card practice in random direction
- Score tracking with percentage and performance feedback
- Cards are shuffled randomly each session
- Case-insensitive answer checking
- Type `q` at any time to exit a mode

## How to Run

Make sure you have Python installed, then run:

```
python flashcard_app.py
```

No external libraries needed — uses only Python's built-in `random` module.

## Example

```
╔══════════════════════════════════════╗
║      🇷🇺  Russian Flashcard App  🇬🇧   ║
╚══════════════════════════════════════╝
  20 cards loaded

Choose a study mode:
  1 — 📖 Study Mode       (flip through all cards)
  2 — ✏️  Quiz Mode        (Russian → English)
  3 — 🔄 Reverse Quiz     (English → Russian)
  4 — 🎲 Random Card      (quick single card practice)
  5 — 🚪 Quit

Question 1/20
  🇷🇺  привет
  Your answer: hello
  ✅ Correct!

========================================
  📊 Your Score: 18/20  (90.0%)
  🌟 Great job! Keep it up!
========================================
```

## How to Add More Words

Open `flashcard_app.py` and add new entries to the `flashcards` list at the top:

```python
{"russian": "кошка", "english": "cat"},
{"russian": "собака", "english": "dog"},
```

## What I Learned

- Using the `random` module (`shuffle`, `choice`)
- Working with **lists of dictionaries**
- Writing a **multi-mode application** with clean function separation
- **String normalization** for flexible answer checking
- Calculating and displaying **percentage scores**
- Designing a real, reusable tool from scratch
