"""
Command line quiz to learn the EU Technology Readiness Level definitions.
Enter q at any time to quit.
"""


import random


# Technology readiness level and description from EU definitions
TRL = {
    9: "Actual system proven in operational environment",
    8: "System complete and qualified",
    7: "System prototype demonstration in operational environment",
    6: "Technology demonstrated in relevant environment",
    5: "Technology validated in relevant environment",
    4: "Technology validated in lab",
    3: "Experimental proof of concept",
    2: "Technology concept formulated",
    1: "Basic principles observed",
}

# Create list from dict for random.choice
TRL_LIST = list(TRL.items())


# Global bool, when set False the game loop & programme end
running = True


class QuizTypeEnum:
    """Enumeration for quiz types."""
    both = 0
    description = 1
    level = 2

    # Possible user input characters to select type of quiz
    input_chars = {
        'b': both,
        'd': description,
        'l': level,
    }


def check_quit(user_input):
    """
    If user input is q, return True and end programme by setting running to
    False, this ends the while loop in main. Else return False.
    """
    if user_input.lower() == 'q':
        global running
        running = False
        return True
    else:
        return False


def choose_quiz_type():
    """
    User picks whether to be tested on level number, description, or both.
    """
    print("Would you like to be tested on level number, description, or both?")
    user_choice = input("Type l, d, or b then press enter to choose.\n")

    # End game loop if user types q
    # Return to prevent execution of the rest of the function
    if check_quit(user_choice): return

    return QuizTypeEnum.input_chars[user_choice]


def description_question():
    """
    User is given the TRL number and must recall the description. When they
    have done this they press enter to reveal the answer.
    """
    level, description = random.choice(TRL_LIST)
    print(f"What happens at level {level}?")
    user_input = input("Press enter to reveal answer:")

    # End game loop if user types q
    # Return to prevent execution of the rest of the function
    if check_quit(user_input): return

    # Print correct answer and space before next question
    print(description)
    print('\n')


def level_question():
    """
    User is given the TRL description and must enter the corresponding level.
    Return True if correct, False if incorrect.
    """
    # Parameter to return if user is correct for score counting
    correct = None

    level, description = random.choice(TRL_LIST)
    print("What level is this?")
    user_input = input(f"{description}\n")

    # End game loop if user types q
    # Return to prevent execution of the rest of the function
    if check_quit(user_input): return

    # Convert input string to int, parse non-numerical input error
    try:
        user_input = int(user_input.strip())
    except ValueError:
        print(f"Incorrect answer format, this is level {level}")

    # Check user answer and inform user accordingly
    if user_input == level:
        print("Correct")
        correct = True
    else:
        print(f"Incorrect, this is level {level}")
        correct = False

    # Final blank line to separate next question
    print('\n')

    return correct


if __name__ == "__main__":
    # User is asked which quiz type they would like to play
    # User enters either 'b', 'l', or 'd' into terminal to choose
    quiz_type = choose_quiz_type()

    # While the loop runs the user is asked questions
    while running:
        # Each loop print a question based on the quiz type
        if quiz_type == QuizTypeEnum.both:
            # Randomly choose question function and call it
            random.choice([description_question, level_question])()
        elif quiz_type == QuizTypeEnum.description:
            # Give level and ask for description, user doesn't enter answer
            description_question()
        elif quiz_type == QuizTypeEnum.level:
            # Give description, user enters level
            level_question()
