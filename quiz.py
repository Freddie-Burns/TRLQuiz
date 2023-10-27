import random


# Technology readiness level and description from EU definitions
trl = {
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
trl_list = list(trl.items())


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


def choose_quiz_type():
    """
    User picks whether to be tested on level number, description, or both.
    """
    print("Would you like to be tested on level number, "
          "description, or both?",)
    user_choice = input("Type l, d, or b then press enter to choose.\n")
    return QuizTypeEnum.input_chars[user_choice]


def description_question():
    """
    User is given the TRL number and must recall the description. When they
    have dones this they press enter to reveal the answer.
    """
    level, description = random.choice(trl_list)
    print(f"What happens at level {level}?")
    input("Press enter to reveal answer:")
    print(description)
    print('\n')


def level_question():
    """
    User is given the TRL description and must enter the corresponding level.
    """
    level, description = random.choice(trl_list)
    print("What level is this?")
    user_answer = input(f"{description}\n")

    try:
        user_answer = int(user_answer.strip())
    except ValueError:
        print(f"Incorrect answer format, this is level {level}")

    if user_answer == level:
        print("Correct")
    else:
        print(f"Incorrect, this is level {level}")

    # Final blank line to separate next question
    print('\n')


if __name__ == "__main__":
    # User is asked which quiz type they would like to play
    # User enters either 'b', 'l', or 'd' into terminal to choose
    quiz_type = choose_quiz_type()

    # While the loop runs the user is asked questions
    running = True
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
