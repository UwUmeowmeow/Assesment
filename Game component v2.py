import random


def quizz():
    score = 0
    questions = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    rounds_played = 0
    while rounds_played < 5:
        question = random.choice(questions)
        attempt = input(f"What is the answer to {question}: ")
        rounds_played += 1
        answer_index = questions.index(question)
        answer = numbers[answer_index]

        if attempt == answer:
            print("CORRECT!\n good job")
            score += 1
        else:
            print("INCORRECT!\n better luck next time")
    return score


# Main rountine
score = quizz()
print(f"You got {score} points")


