# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes  / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

   **** Instructions ****

     To begin, choose the number of questions you'd like to do (or
    press <enter> for infinite mode). Then you'll be asked some math 
    questions.

    Press <xxx> to end the quiz anytime.

   Good luck.

    ''')


# Main routine
print()
print("🧠🧠🧠 Math Quiz 🧠🧠🧠")
print()

# loop for testing purposes

want_instruction = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instruction == "yes":
    instruction()

# print("program continues")