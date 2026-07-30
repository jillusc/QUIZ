# QU!ZZ!CAL

Quizzical is a terminal-based multiple-choice quiz game written in Python.

Players test their knowledge across three question packs of general knowledge questions, receive immediate feedback on their answers and have their scores recorded in a Google Sheets leaderboard.

Originally created as a study project in 2023, Quizzical has since been updated to run locally using a modern Node.js environment while preserving the original gameplay and Google Sheets integration.

![Responsive preview](README%20documentation/quizzical-amiresponsive.jpg)

The live app can be viewed here: <a href="https://quizzical-ll20.onrender.com/">QU!ZZ!CAL</a>

## How it works

The player is prompted to enter a username, which is used to record their score on the leaderboard.

Three question packs are available. After completing a round, the player can choose to continue with another pack or finish the game.

Each question presents three possible answers. The player selects their answer by entering **A**, **B** or **C** on their keyboard.

After each answer, feedback is given. Incorrect answers do not reveal the correct option, encouraging players to replay and improve their score.

At the end of the game, the player's score is stored in a Google Sheets database. The player can then view a leaderboard displaying the five highest scores.

## Features

### Current features

- Welcome screen with title graphic and game instructions:

![Welcome screen](README%20documentation/welcome_screen.jpg)

- Username entry with input validation and clear error messages:

  ![Validation](README%20documentation/quizzical_error_handling.webp)

- Selection of three different question packs:

  ![Question pack selection](README%20documentation/Q_pack_selection.jpg)

- Questions are randomly shuffled each time a pack is played

- Ten multiple-choice questions per pack

- Immediate feedback after each answer:

![Gameplay](README%20documentation/questions.jpg)

- Score displayed at the end of each round

- Option to continue playing another question pack

- Game over screen with option to view leaderboard:

![End of game](README%20documentation/end_of_game.jpg)

- Top five leaderboard stored in Google Sheets:

![Leaderboard](README%20documentation/leaderboard.jpg)

- Integration with Google Sheets using the gspread library

- Leaderboard displayed in the terminal using the **tabulate** library.

## Technologies

- Python
- Node.js
- Total.js
- Google Sheets API
- gspread
- tabulate

## Running locally

Clone the repository:

```bash
git clone https://github.com/jillusc/QUIZ.git
```

Install the Node.js dependencies:

```bash
npm install
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create a `creds.json` file containing your Google service account credentials.

Start the application:

```bash
node index.js
```

The application will then be available at:

```
http://localhost:8000
```

## Future improvements

- Allow players to accumulate a total score across all three question packs
- Display each question in a freshly cleared terminal
- Calculate and display scores as percentages
- Prevent duplicate usernames
- Add additional themed question packs
- Randomise the answer order as well as the questions.

## Design

The interface was intentionally kept clean and uncluttered to resemble a traditional terminal application.

- Black background with a centred terminal
- Gold title text for contrast
- Google Font used for the title text
- Subtle vertical stripe added to balance the page visually alongside the scrollbar.

## Testing

### Bugs resolved

- Long questions wrapped awkwardly in the terminal and were reformatted
- Scoreboard updates were corrected by ensuring scores are written to Google Sheets before being displayed
- Screen clearing was adjusted so that important messages remain visible long enough to be read.

### Known limitations

The first three items listed under **Future improvements** remain planned enhancements.

### Validation

The Python code passes linting without errors:

![Linter](README%20documentation/python-linter-pass.webp)

## Credits

### Resources

- Code Institute's original terminal application project
- Google Sheets API
- gspread
- tabulate

### Inspiration

Some Python techniques were inspired by the Code Institute learning materials before being adapted for this project.

Additional troubleshooting and modernisation of the project for local development was carried out with assistance from ChatGPT.
