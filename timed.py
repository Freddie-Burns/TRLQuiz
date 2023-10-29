"""
How many level numbers can you correctly identify in 1 minute?
"""


import time
import quiz


RACE_LENGTH = 60  # seconds


def play():
    """
    Give level number from description. Give questions and record score until
    time runs out. Print user's score at the end.
    """
    start = time.time()
    score = 0

    while time.time() - start < RACE_LENGTH:
        score += int(quiz.level_question())

    print(f"Your score is {score}")
    time.sleep(1)


if __name__ == "__main__":
    running = True
    while running:
        play()
        replay = input("Play again?\n")
        if 'y' not in replay.lower():
            running = False
