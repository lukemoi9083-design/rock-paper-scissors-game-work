"""Game rules and name checking. No database and no window code here."""
import random
import re


class Game:
    CHOICES = ["rock", "paper", "scissors"]

    def computer_choice(self):
        """The computer picks a random move."""
        return random.choice(self.CHOICES)

    def get_result(self, player, computer):
        """Return 'win', 'lose' or 'draw' for the player."""
        if player == computer:
            return "draw"
        if player == "rock" and computer == "scissors":
            return "win"
        if player == "paper" and computer == "rock":
            return "win"
        if player == "scissors" and computer == "paper":
            return "win"
        return "lose"


def check_name(name):
    """Use a regex to check the name. Returns the clean name or raises ValueError."""
    name = name.strip()
    # ^ start, [A-Za-z0-9_-] allowed characters, {3,20} length 3 to 20, $ end
    if not re.match(r"^[A-Za-z0-9_-]{3,20}$", name):
        raise ValueError("Name must be 3-20 characters long and contain only letters, numbers, underscores or hyphens.")
    return name
