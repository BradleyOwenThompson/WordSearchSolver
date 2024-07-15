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


def is_viable(x_candidate, y_candidate, x_step, y_step):
    """Check if a requested step is within the board"""
    max_y, max_x = game_grid.shape

    if (
        (x_candidate + (x_step) >= 0)
        and (x_candidate + (x_step) < max_x)
        and (y_candidate + (y_step) >= 0)
        and (y_candidate + (y_step) < max_y)
    ):
        return True
    else:
        return False


def follow_path(word, x_position, y_position, x_offset, y_offset):
    "Check if the journey leads to the word"
    characters_matched = 0
    for step, character in enumerate(word):
        if (
            character
            == game_grid[y_position + (y_offset * step), x_position + (x_offset * step)]
        ):
            characters_matched += 1
        else:
            break
    if characters_matched == len(word):
        return True
    else:
        return False


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
                # Check if it can follow a valid path
                if follow_path(word, coordinate_x, coordinate_y, mask[0], mask[1]):
                    print(
                        f"{word}: ({coordinate_x}, {coordinate_y}) -> "
                        f"({coordinate_x+((len(word)-1) * mask[0])}, "
                        f"{coordinate_y + ((len(word)-1) * mask[1])})"
                    )
