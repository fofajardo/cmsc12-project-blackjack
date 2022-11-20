import game
import scores
import utils

# The available menu items.
MENU_ITEMS = {
    # Switches to the main game scene.
    "1": {
        "label": "Play",
        "action": game.run
    },
    # Switches to the high score scene.
    "2": {
        "label": "View High Scores",
        "action": scores.run
    },
    # Exits the game.
    "0": {
        "label": "Exit",
        "action": exit
    }
}

# Start sequence: prints the intro and performs menu processing.
def start():
    for i in utils.strings["intro_mm"]:
        print(i.center(80))
    print()

    while True:
        utils.process_menu(MENU_ITEMS)

start()
