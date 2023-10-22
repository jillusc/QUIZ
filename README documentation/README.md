# QUIZZICAL

Quizzical is a multiple-choice quiz game to be played in a Python terminal - it runs in a mock terminal provided by Code Institute on Heroku.
Users can test their knowledge and have fun playing through three rounds of miscellaneous questions.

<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-amiresponsive.webp">

The live version can be found here: <a href="https://quizzically-6a77b78fbbe8.herokuapp.com/">QUIZZICAL</a>


## How it works

The player is prompted to enter their name for the purposes of adding their scores to the scoreboard. This can inspire an element of competition, and therefore mean the user invests more in the game.<br><br>
A total of three question packs are available to play through: the user chooses which one to play, and at the end of that round has the option to continue to another question pack.<br><br>
Questions are presented along with three optional answers for the player to choose from: they must input A, B or C.<br><br>
Answers are confirmed as correct or incorrect. With an incorrect guess, players are not informed of the right answer in order to encourage playing again!<br><br>
The score achieved by the player, along with their inputted username, is added to a database in the form of a Google sheet.<br><br>
At the end of the game, a scoreboard can be viewed - it presents the top five highest scores in descending order.


## Features

### Exising features:
* The user is welcomed and introduced to the game via a visual graphic:<br>
* The player's input is requested:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-screen1.webp">


* Data entered is validated and error-handling is accounted for:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical error handling.webp">


* A second visual graphic presents the user with options to select from Question Pack 1, 2 or 3:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-screen2.webp">


* The questions from the relevant pack are shuffled by the computer:<br>
* One by one, ten questions are displayed along with multiple choice answers:
* The player receives a positive response when they guess correctly; the response for a wrong answer is neutral and not negative:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-screen3.webp">


* Scores are accrued and the player is informed of their score for the round:<br>
* They can opt to play again:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-screen3b.webp">


* A game over visual appears when the player chooses not to play again:<br>
* They can opt to view the scoreboard:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-screen4.webp">


* The scoreboard shows the top five highest scores:
* The player's input actively ends the game:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical-screen5.webp">


* Data manipulation is used to interact with a Google Sheet via the gspread library:
* Data is stored in the worksheet; it is retrieved in the program and returned as a list:
* In the terminal, the data is displayed in a table using the tabulate 0.9.0 library:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/quizzical scoresheet.webp">



### Features to implement:
* To account for a player opting to work through all three question packs and thus accumulate the scores for each round, i.e. with a total score out of 30
* It would be more visually pleasing if each question appeared on a blank terminal - by preceding each one with the clear() method, for example
* A method by which scores are calculated as a percentage would be preferable
* More control over username would be useful, e.g. not accepting a conflicting name
* More sets of questions can be easily added; they could also be categorised (music, history, food & drink, etc.)
* The answer options could also be shuffled before being presented to the player for a more interesting return experience


### Style
* A plain and uncluttered aesthetic was intended: this instills a sense of seriousness and may aid the user's mental clarity
* A nice, clean black background was added to the page and the terminal centred for visual effect
* Contrasting gold text was used for the title
* The title's font was imported from Google Fonts and was selected to uphold the feel of raw, 'terminal' text, being reminiscent of symbols
* The Run Program button was styled in the same scheme
* A vertical grey stripe was added to visually balance the scrollbar of the terminal, taking the same colour (#f1f1f1)


## Testing

### Bugs:
* The first three items in 'Features to implement' above were attempted but as yet remain unresolved

* Resolved- Feedback from testing included a couple of longer questions not displaying well, whereby words were broken up at the right-hand edge of the terminal: this was easily resolved by placing a '/n' at relevant positions in the text
* Resolved- I found that the player's score wasn't showing on the scoreboard: I discovered that the reason for this was that the display_scores function was being called before the update_scores function
* Resolved- Another issue was not seeing text printed to the terminal: I realised this was due to the usage of the clear() function and that the terminal was cleared immediately after the print(), meaning simply that the eye had no time to register it

### Validation:
* The code was passed through a Python linter and received no errors:
<img src="https://github.com/jillusc/QUIZ/blob/main/README%20documentation/python-linter-pass.webp">


## Deployment

Quizzical was deployed using Code Institute's mock terminal


