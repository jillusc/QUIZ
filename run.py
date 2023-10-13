import gspread
from google.oauth2.service_account import Credentials
import json
from questions import question_packs
import random

# ANSI escape codes for colours
YELLOW = "\033[33m"
RESET = "\033[0m"

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
    The input string begins with spaces in
    order to position the text with an apt indent.
    """
    with open('welcome_screen.txt', 'r') as file:
        content = file.read()
    print(content)

    while True:
        try:
            name = input("        To start, please enter a username: ")
            if not name.strip():
                raise ValueError("A username is required.")
            if not (3 <= len(name) <= 10 and name.isalnum()):
                raise ValueError("Username must be 3-10 alphanumeric characters.")
        except ValueError as e:
            print(f"Invalid. {e}\n")
        else:
            print()
            print(f"Let's go then, {name}.")
            return name

welcome_screen()

def display_positive_response(name):
    """
    The computer generates a random response
    to a correct answer given by the user.
    """
    positive_responses = [
        "Well done.",
        f"Nice one, {name}.",
        f"Good call, {name}.",
        "Great.",
        "That's right.",
        "Very good."
    ]
