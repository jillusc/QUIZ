import gspread
from google.oauth2.service_account import Credentials
import json
from questions import question_packs
from responses import positive_responses

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("QUIZ. scoreboard")

scores = SHEET.worksheet("scoresheet")

data = scores.get_all_values()
print(data)
