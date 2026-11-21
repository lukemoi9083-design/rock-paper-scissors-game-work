# Rock Paper Scissors

Casual games have no memory of who is winning, so this app lets players create profiles, play Rock Paper Scissors against the computer and keeps each player's win, loss and draw record between sessions.

## Project Description

Rock Paper Scissors is a Python desktop application built with Tkinter. Players can create profiles, play against a computer opponent and view their statistics and recent match history. All data is stored in an SQLite database, so it is still there the next time the app is opened.

## Features

- Play Rock Paper Scissors against a computer opponent that chooses randomly.
- Create, rename and delete player profiles.
- Track wins, losses and draws for each player.
- View the last 10 matches for the selected player.
- Save players and matches in SQLite so data is kept between sessions.
- Validate player names with regular expressions.
- Show friendly error messages instead of crashing.
- Use a graphical user interface built with Tkinter.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical user interface |
| SQLite | Database and data storage |
| Regular expressions | Player name validation |
| python-dotenv | Loading the database name from a `.env` file |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
rock-paper-scissors/
├── main.py
├── ui.py
├── game.py
├── database.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

- `main.py`: starts the application.
- `ui.py`: the window, buttons and user interactions.
- `game.py`: the game rules and player name validation.
- `database.py`: creates the database and handles players and matches.
- `requirements.txt`: the external Python packages needed.
- `.gitignore`: keeps private and generated files (`.venv/`, `__pycache__/`, database files and `.env`) out of GitHub.
- `.env.example`: an example of the local settings file.

## Installation and Setup

### Requirements

- Python 3 installed on your computer.
- Git installed on your computer.
- Visual Studio Code or another Python editor.

### 1. Clone the repository

```bash
git https://github.com/lukemoi9083-design/rock-paper-scissors-game-work.git
```


### 2. Open the project folder

```bash
cd rock-paper-scissors
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell says running scripts is disabled, run this first and then try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Git Bash:

```bash
source .venv/Scripts/activate
```

### 5. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Create your environment file

Copy `.env.example` and name the copy `.env`.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Git Bash:

```bash
cp .env.example .env
```

The only setting is the database file name:

```text
DB_NAME=rps.db
```

If there is no `.env` file, the app uses `rps.db` by default.

### 7. Start the application

```bash
python main.py
```

## How to Play

1. Type a name in the text box and click **Add player**.
2. Make sure the player is selected in the dropdown.
3. Click **Rock**, **Paper** or **Scissors**.
4. The computer picks its move at random and the result is shown.
5. The wins, losses and draws, and the last 10 matches, update after every round.
6. Use **Rename player** or **Delete player** to manage profiles. Deleting a player also deletes their matches.

## The Window

From top to bottom, the window shows:

- The title "Rock Paper Scissors".
- A dropdown to choose the current player.
- A text box and the **Add player**, **Rename player** and **Delete player** buttons.
- The **Rock**, **Paper** and **Scissors** buttons.
- The result of the latest round.
- The selected player's wins, losses and draws.
- A list of their last 10 matches.

## Player Names

Names must:

- be between 3 and 20 characters long,
- use only letters, numbers, underscores or hyphens,
- be unique.

A regular expression checks the characters and length. Invalid names show a friendly message.

## Database

SQLite saves the data in two tables:

- `players`: the player ID and unique name.
- `matches`: the player, their choice, the computer's choice and the result.

All queries that use input values use `?` placeholders, which helps protect against SQL injection. The app supports all four database operations:

- **Create:** add a player, save a match.
- **Read:** list players, show matches and statistics.
- **Update:** rename a player.
- **Delete:** delete a player and their matches.

## Error Handling

Database code is wrapped in `try/except`. If something goes wrong, or the input is invalid (for example a name that is too short or already taken), the app shows a clear message in a pop-up window instead of crashing.

## Screenshots

Screenshots are not included yet.

## Author

luke moi
