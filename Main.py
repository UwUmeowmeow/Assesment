import random

quest_no = 0


# Get username
def get_name():
    your_name = input("What is your name: ")
    return your_name


# Get user age
def get_age():
    your_age = input("How old are you: ")
    return your_age


# Get difficulty and check if it is valid
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


# Main quizz
def quizz():
    scores = 0
    global quest_no
    # list of numbers in maori and numbers
    questions = ["tahi", "rua", "toru", "whā", "rima",
                 "ono", "whitu", "waru", "iwa", "tekau"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    rounds_played = 0
    # if mode is easy, number of question is 5
    if mode == 'easy' or mode == 'e':
        quest_no = 5
    # else number of question is 10
    else:
        quest_no = 10
    # Check answer if correct or not, check rounds and scores
    while rounds_played < quest_no:
        rounds_played += 1
        # Randomly choose one questions
        question = random.choice(questions)
        attempt = input(f"{rounds_played}. What is the answer to {question}: ")
        # get answer using index
        answer_index = questions.index(question)
        answer = numbers[answer_index]
    # Check answer if it is correct or not
        if attempt == answer:
            print("CORRECT!\ngood job")
            scores += 1
        else:
            print("INCORRECT!\nbetter luck next time\n"
                  f"The correct answer is "
                  f"{numbers[questions.index(question)]}\n")
    return scores


# Check if user say yes or no
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
            print("Please enter 'yes' or 'no'")


# Show user instructions of how to play
def instructions():
    print("\n*** How to play ***")
    print()
    print("This is a Maori numbers quiz\n"
          "which you answer the number 1,2,3,..., 10 "
          "from the name that is given\n"
          "and match the choice then add the up the score.\n")
    print()


# Main routine
print("\tWelcome to Ngā Tau pātai\n"
      "--------------------------------")

name = get_name()
age = get_age()

print(f"\nHi {name} At {age} you might find this quiz little bit easy.\n"
      f"They are 5, 10 question selected by your difficulty.\n")

played_before = yes_no("Have you play before?: ")
# if user have not played before, show instructions
if played_before == "No":
    instructions()

mode = difficulty()
score = quizz()
# Show user their scores
print(f"You got {score} points out of {quest_no} ")
print("** Thank for playing **")
