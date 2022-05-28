print("\tWelcome to Ngā Tau pātai\n"
      "--------------------------------")


def get_name():
    your_name = input("What is you name: ")
    return your_name


def get_age():
    your_age = input("How old are you: ")
    return your_age


# Main routine
name = get_name()
age = get_age()
print(f"\nHI {name}. At {age} year old, you might find this quizz a bit easy.")
