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
    print("Program continues")
    print()


played_before = yes_no("Have yo play before?: ")

if played_before == "No":
    instructions()
else:
    print("Program continues")
