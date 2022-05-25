show_instructions = ""
while show_instructions != "x":

    show_instructions = input("Have you play this game before?: ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues\n")

    elif show_instructions == "no" or show_instructions == "n":
        print("This is a Maori numbers quizz\nwhich you answer the number 1,2,3,..., 10 from the name that is given\n"
              "and match the choice then add the up the score")

    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered '{show_instructions}' ")
