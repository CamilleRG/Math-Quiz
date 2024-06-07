import random


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

            # checks that the number is more than 1
            if response < 1:
                print(error)
                # return "invalid"

            else:
                return response

        except ValueError:
            print(error)


def num_checker(question):
    while True:
        error = "Please enter a valid number."

        to_check = input(question)

        # check for infinite mode / exit code
        if to_check == "xxx":
            return to_check

        try:
            response = int(to_check)

            # checks that the number is more than 1
            if response < 0:
                print(error)
                # return "invalid"
            else:
                return response

        except ValueError:
            print(error)


# ask user math questions
def addition_operation():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    return num_1, num_2, num_1 + num_2, '+'


def subtraction_operation():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    # making sure question have non-negative results
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1
    return num_1, num_2, num_1 - num_2, '-'


def multiplication_operation():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    return num_1, num_2, num_1 * num_2, '*'


def division_operation():
    while True:
        divisor = random.randint(1, 10)
        quotient = random.randint(1, 10)
        dividend = divisor * quotient

        return dividend, divisor, quotient, '/'


# Main Routine Starts here

# Initialise quiz variables
mode = "regular"
end_quiz = "no"
question_asked = 0
ans_wrong = 0

operations = [
    addition_operation,
    subtraction_operation,
    multiplication_operation,
    division_operation
]
quiz_history = []

print()
print("🧠🧠🧠 Math Quiz 🧠🧠🧠")
print()

# ask user if they want to see the instruction and display
# them if requested
want_instruction = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instruction == "yes":
    instruction()

# quiz_difficulty = difficulty_mode("Please choose a difficulty mode ( Easy | Medium | Hard): ").lower()

# Ask user for the number of questions / infinite mode
num_question = int_check("How many questions would you like to do? push <enter> for infinite mode: ")

if num_question == "infinite":
    mode = "infinite"
    num_question = 5

# ask for quiz difficulty


# Quiz loop starts here
while question_asked < num_question:

    # Quiz Heading
    if mode == "infinite":
        quiz_heading = f"\n ❓❓❓ Question {question_asked + 1} (Infinite Mode) 💥💥💥"

    else:
        quiz_heading = f"\n ❓❓❓ Question {question_asked + 1} of {num_question} 💥💥💥"

    print(quiz_heading)

    # Questions starts here

    # get user answer
    operation = random.choice(operations)
    num_1, num_2, correct_answer, symbol = operation()

    # ask the user the math question
    user_answer = num_checker(f"What is {num_1} {symbol} {num_2}? ")

    # If user answer is the exit code, break the loop
    if user_answer == "xxx":
        break

    # feedbacks to user's answers
    try:
        # user_answer = int(user_answer)
        if int(user_answer) == correct_answer:
            feedback = "🥳🥳🥳 Congratulations! Your answer is correct. 🥳🥳🥳"
        else:
            ans_wrong += 1
            feedback = f"🥲🥲🥲 Sorry, the correct answer is {correct_answer} 🥲🥲🥲"
    except ValueError:
        feedback = "Please enter a valid number."

    print(feedback)

    # if user has entered exit code, end quiz!!
    if end_quiz == "yes":
        break

    # Quiz ends here

    # If user answer is the exit code, break the loop
    if user_answer == "xxx":
        break

    # Add the question result in the quiz history
    history_feedback = f"Question {question_asked + 1}: {feedback}"
    quiz_history.append(history_feedback)

    question_asked += 1

    # if users are in infinite mode, increase number of questions!
    if mode == "infinite":
        num_question += 1

# check users have played at least one round
# before calculating statistics
if question_asked > 0:
    # Calculate Statistics
    ans_right = question_asked - ans_wrong
    percent_right = ans_right / question_asked * 100
    percent_wrong = ans_wrong / question_asked * 100

    print()
    # Output Quiz Statistics
    print("📊📊📊 Quiz Statistics 📊📊📊")
    print(f"🥳 Right: {percent_right: .2f} \t "
          f"😢 Wrong: {percent_wrong:.2f} \t ")

    # ask user if they want to see their quiz history and output it if requested.
    see_history = yes_no("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print()
    print("Thanks for playing.")

# If users quit without playing a round
else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")



