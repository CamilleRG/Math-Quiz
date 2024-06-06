# checks the uer enters an integer
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            print(error)
            # return "invalid"



# Initialise quiz variables
mode = "regular"

question_asked = 0


print()
print("🧠🧠🧠 Math Quiz 🧠🧠🧠")
print()


# Ask user for the number of questions / infinite mode
num_question = int_check("How many questions would you like to do? push <enter> for infinite mode: ")

if num_question == "infinite":
    mode = "infinite"
    num_question = 5


# Quiz loop starts here
while question_asked < num_question:

    # Quiz Heading
    if mode == "infinite":
        quiz_heading = f"\n ❓❓❓ Question {question_asked + 1} (Infinite Mode) 💥💥💥"

    else:
        quiz_heading = f"\n ❓❓❓ Question {question_asked + 1} of {num_question} 💥💥💥"

    print(quiz_heading)


# get user answer
    user_answer = input("Answer? ")

    # If user choice is the exit code, break the loop
    if user_answer == "xxx":
        break

    question_asked += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_question += 1.
