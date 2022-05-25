import random


def get_name():
    your_name = input("What is you name: ")
    return your_name


def get_age():
    your_age = input("How old are you: ")
    return your_age


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


def yes_no(question_text):
    while True:

        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer == "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Please enter 'yes' or 'no'")\



def instructions():
    print("**** How to play ****")
    print()
    print("This is a Maori numbers quizz\n which you answer the number 1,2,3,..., 10 from the Maori name that is given")
    print()
# Main routine


print("\tWelcome to Ngā Tau pātai\n"
      "--------------------------------")
name = get_name()
age = get_age()
print("This is a Maori numbers quizz\nwhich you answer the number 1,2,3,..., 10 from the name that is given\n"
              "and match the choice then add the up the score\n")

played_before = yes_no("Have yo play before?: ")

if played_before == "No":
    instructions()


score = quizz()
print(f"**** You got {score} points ****")
print("********* Thank for playing *********")
print("*", "Goodbye", "*")
