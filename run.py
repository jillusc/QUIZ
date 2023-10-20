# Lines 1-3 copied from Love Sandwiches walkthrough
import gspread
from google.oauth2.service_account import Credentials
import json
from questions import question_packs
import random
import os
from tabulate import tabulate

# ANSI escape codes for colours
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Lines 15-28 copied from Love Sandwiches walkthrough
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Quizzical scoreboard")

scores = SHEET.worksheet("scoresheet")
data = scores.get_all_values()


def welcome_screen():
    """
    The first view for the user:
    via the txt file, the game is explained;
    then the function requests username input
    and validates the data entered.
    The input string and the final message both
    begin with spaces in order to position the
    text with an apt indent.
    """
    with open('welcome_screen.txt', 'r') as file:
        content = file.read()
    print(content)

    while True:
        try:
            name = input("         To start, please enter a username: ")
            if not name.strip():
                raise ValueError("A username is required.")
            if not (3 <= len(name) <= 10 and name.isalnum()):
                raise ValueError("Username must be 3-10 alphanumeric "
                                 "characters.")
            if not any(c.isalpha() for c in name):
                raise ValueError("Username must contain at least one letter.")
        except ValueError as e:
            print(f"\033[33mInvalid:\033[0m {e}\n")
        else:
            print()
            print(f"         Let's go then, {name}.")
            return name


def choose_question_pack():
    """
    This function loads the visual of question packs
    and requests the user to select one of the three
    sets of 10 questions (which are stored in
    questions.py); validates inputted data.
    """
    with open('question_pack_visual.txt', 'r') as file:
        content = file.read()
        print(content)

        while True:
            try:
                questions = (input("Choose a question pack: "))
                if questions not in ['1', '2', '3']:
                    raise ValueError("please enter 1, 2, or 3.")
            except ValueError as e:
                print(f"\033[33mInvalid:\033[0m {e}\n")
            else:
                clear()
                print(f"Alright! Question pack {questions} it is.\n")
                return questions


# The function below uses third party code found here:
# https://github.com/Inc21/Python-Quiz-Game-PP3/blob/main/run.py
def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
    """
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Mac and Linux
    else:
        os.system('clear')


def run_game(question_pack, name):
    """
    The main game function. It shuffles and then displays
    the questions and the answer options that are stored
    in questions.py. Then it prompts the user's answer
    input, validates it for A, B or C only, evaluates
    the answer, provides an appropriate response,
    increments the score. Finally, it returns the score,
    passing the value to the end_of_game function.
    """
    score = 0
    question_number = 1
    positive_responses = [
        "Well done.",
        f"Nice one, {name}.",
        f"Good call, {name}.",
        "Great.",
        "Alright.",
        "Very good."
    ]

    random.shuffle(question_pack["questions"])

    for question_data in question_pack["questions"]:
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]

        print(f"Q{question_number}. {question}\n")

        for option in options:
            print(option)
        print()
        while True:
            user_answer = input("What's your answer: A, B or C? ").upper()
            if user_answer in ["A", "B", "C"]:
                break
            else:
                print("Invalid answer. Please enter A, B or C.")
                print()

        if user_answer.upper() == correct_answer:
            response = random.choice(positive_responses)
            print(f"\033[32mCorrect! {response}\033[0m\n")
            score += 1
        else:
            print(f"\033[33mSorry! That's incorrect.\033[0m\n")
            print()

        question_number += 1

    return score


def end_of_game(score, name):
    """
    This function handles the score returned from the main
    run_game function: it informs the user that the round has
    ended, prints the score with an appropriate response.
    Finally, it asks the user if they want to play another
    round and deals with Y by looping back to the question
    packs visual, and N by printing a final message.
    """
    print("That's the end of this round!")
    print(f"You scored {score}/10\n")

    if score <= 4:
        print(f"Thanks for playing, {name} :)\n")
    elif score in range(5, 8):
        print(f"Not bad, {name}!\n")
    else:
        print(f"That's a great score! Well played, {name}!\n")

    update_scoresheet(name, score)

    play_again = input("Do you want to play another round? (Y/N): ").upper()

    if play_again == "Y":
        clear()
        print("Great!")
        return True
    elif play_again == "N":
        print()
        show_scoreboard = input("Would you like to see the scoreboard? "
                                "(Y/N): ").upper()
        if show_scoreboard == "Y":
            display_scores(data)
        print()
        print("Thank you for playing Quizzical!\n")
        print("Have a good day!")
        print()
        input("Enter Q to quit: ").upper()
        clear()

        main_game_loop()
        return False


def update_scoresheet(name, score):
    """
    This takes the name and score values and
    adds them to the Google scoresheet. First, the
    score is converted to a % of the total
    possible score (30). E.g. a score of 30/30 = 100%.
    """
    try:
        scores.append_row([name, score])
        print()
        print(f"Your score is being added to the scoreboard...")
        print()
    except Exception as e:
        print(f"\033[33mAn error occurred: {e}\033[0m")
        while True:
            try_again = input("Do you want to try again? "
                              "(Y/N): ").strip().upper()
            if try_again == "Y":
                return update_scoresheet(name, score)
            elif try_again == "N":
                print("Returning to start...")
                return
            else:
                print("Invalid input. Please enter Y or N.")


def display_scores(data):
    """
    This displays the username and (top 5) scores from the
    Google sheet in a table using tabulate, first using
    a method to sort the data into descending order.
    """
    clear()
    print("Top 5 scores:")
    print()
    headers = data[0]
    scoresheet_data = data[1:]
    # Line 236 contains code taken offered by Tomas_K_5P on Slack:
    # https://app.slack.com/client/T0L30B202/D061PFKHFFD
    sorted_scores = sorted(scoresheet_data, key=lambda x: float(x[1]),
                           reverse=True)
    top_5_scores = sorted_scores[:5]
    table = tabulate(top_5_scores, headers=headers, tablefmt="pretty")
    print(table)


def main_game_loop():
    """
    This function defines the loop of the whole game.
    """
    name = welcome_screen()
    if name is None:
        return

    total_score = 0

    while True:
        questions = choose_question_pack()
        if not questions:
            break

        score = run_game(question_packs[int(questions)], name)
        total_score += score

        play_again = end_of_game(score, name)
        if not play_again:
            break


main_game_loop()
