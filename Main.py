import random

quest_no = 0


def get_name():
    your_name = input("What is you name: ")
    return your_name


def get_age():
    your_age = input("How old are you: ")
    return your_age


def difficulty():
    valid = False
    while not valid:
        error = "Please choose easy/hard\n"
        try:
            print("Choose 1 difficulty:\n"
                  " - Easy\n"
                  " - Hard")
            difficult = input(">>> ").lower()
            if difficult == "easy" or difficult == "e":
                print("You chose easy mode you going to answer 5 questions\n")
                return difficult
            elif difficult == 'hard' or difficult == 'h':
                print("You chose hard mode you going to answer 10 questions\n")
                return difficult
            else:
                print(error)
        except ValueError:
            print(error)


def quizz():
    scores = 0
    global quest_no

    questions = ["tahi", "rua", "toru", "whā", "rima",
                 "ono", "whitu", "waru", "iwa", "tekau"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    rounds_played = 0
    if mode == 'easy' or mode == 'e':
        quest_no = 5
    else:
        quest_no = 10

    while rounds_played < quest_no:
        rounds_played += 1
        question = random.choice(questions)
        attempt = input(f"{rounds_played}. What is the answer to {question}: ")
        answer_index = questions.index(question)
        answer = numbers[answer_index]

        if attempt == answer:
            print("CORRECT!\ngood job")
            scores += 1
        else:
            print("INCORRECT!\nbetter luck next time\n"
                  f"The correct answer is "
                  f"{numbers[questions.index(question)]}\n")
    return scores


def yes_no(question_text):
    while True:
        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Please enter 'yes' or 'no'")\



def instructions():
    print("\n*** How to play ***")
    print()
    print("This is a Maori numbers quizz\n"
          "which you answer the number 1,2,3,..., 10 "
          "from the name that is given\n"
          "and match the choice then add the up the score.\n")
    print()
# Main routine


print("\tWelcome to Ngā Tau pātai\n"
      "--------------------------------")

name = get_name()
age = get_age()

print(f"\nHi {name} At {age} you might find this quizz little bit easy.\n"
      f"They are 5, 10 question selected by your difficulty.\n")

played_before = yes_no("Have you play before?: ")

if played_before == "No":
    instructions()

mode = difficulty()
score = quizz()
print(f"You got {score} points out of {quest_no} ")
print("** Thank for playing **")
