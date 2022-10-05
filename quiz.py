# quiz.py

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
    for label, alternative in labeled_alternatives.items():
        print(f"    ({label}) {alternative}")

    while (answer_label := input("\nChoice ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")