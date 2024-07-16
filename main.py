import numpy as np

game_grid = np.array(
    [
        [i for i in "DICORALREEFT"],
        [i for i in "ESDNLFGSEALA"],
        [i for i in "BTAOLBITENIN"],
        [i for i in "MARLINGNENUK"],
        [i for i in "PBBLSEDUDSDG"],
        [i for i in "EURLMMONRIDA"],
        [i for i in "LBDRIONUCGNN"],
        [i for i in "IBCANCHORRLG"],
        [i for i in "CLOWNFISHCCE"],
        [i for i in "AETSITNEDEHL"],
        [i for i in "NSBRUCENNEUL"],
        [i for i in "GILLLIDORYME"],
        [i for i in "YLBARRACUDAN"],
        [i for i in "SKRAHSHPEACH"],
    ]
)

words = [
    "FINDING",
    "NEMO",
    "ELLEN",
    "MARLIN",
    "CLOWNFISH",
    "COREALREEF",
    "PELICAN",
    "BARRACUDA",
    "DORY",
    "SHARKS",
    "BRUCE",
    "ANCHOR",
    "CHUM",
    "DENTIST",
    "TANKGANG",
    "GILL",
    "BLOAT",
    "BUBBLES",
    "PEACH",
    "GURGLE",
    "DEB",
]

masks = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def is_viable(x_candidate: int, y_candidate: int, x_step: int, y_step: int) -> bool:
    """Check if a requested step is within the board"""
    max_y, max_x = game_grid.shape

    if (0 <= (x_candidate + x_step) < max_x) and (0 <= (y_candidate + y_step) < max_y):
        return True
    else:
        return False


def follow_path(
    word: str, x_position: int, y_position: int, x_offset: int, y_offset: int
) -> bool:
    "Check if the journey leads to the word"
    # Skip the first character, check if characters are in sequence
    for step, character in enumerate(word[1:], start=1):
        if (
            character
            != game_grid[y_position + (y_offset * step), x_position + (x_offset * step)]
        ):
            return False

    return True


# Find each word
for word in words:
    # Get the coordinates of the first character
    first_letter_coordinates = np.transpose((word[0] == game_grid).nonzero())

    # Check each candidate coordinate
    for coordinate_y, coordinate_x in first_letter_coordinates:

        # Go through each mask, checking if it's valid
        for mask in masks:
            if is_viable(
                coordinate_x,
                coordinate_y,
                ((len(word) - 1) * mask[0]),
                ((len(word) - 1) * mask[1]),
            ):
                # Check if it follows a valid path
                if follow_path(word, coordinate_x, coordinate_y, mask[0], mask[1]):
                    print(
                        f"{word}: ({coordinate_x}, {coordinate_y}) -> "
                        f"({coordinate_x + ((len(word)-1) * mask[0])}, "
                        f"{coordinate_y + ((len(word)-1) * mask[1])})"
                    )
                    break
