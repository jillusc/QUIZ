import gspread
from google.oauth2.service_account import Credentials
import json
from questions import question_packs

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
print("are you there")


def welcome_screen():
    """
    The first view for the user:
    via the txt file, the game is explained;
    then the function requests username input
    and validates the data entered.
    """
    with open('welcome_screen.txt', 'r') as file:
        content = file.read()
    print(content)

    while True:
        name = input("        To start, please enter a username: ")
        if 3 <= len(name) <= 10 and name.isalnum():
            print(f"Let's go, {name}.")
            return name
        else:
            print("Username must be 3-10 alphanumeric characters.")
            print("Please try again...")
    print()
    print(f"Let's go, {name}.")
    return name


welcome_screen()
