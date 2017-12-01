import random

# ---------
# CONSTANTS
# ---------

MUST_HAVE_STUFFS = [
    "Electric Controller",
    "Bed",
    "Light"
]

EXTRA_STUFFS = [
    "Fridge",
    "Bookcase",
    "Plant",
    "3-dot Brick",
    "Air Ventilation",
    "Book Case",
    "Towel",
    "Computer",
    "Shoes",
    "Fan",
    "Table",
    "Air Conditioner",
    "Wardrobe",
    "Screen",
    "Fish Tank"
]

OPTIONAL_ITEMS = {
    "Computer": ["Left", "Right"],
    "Bed": ["Left", "Right"],
    "Table": ["Speaker", "Cup", "Books"],
    "Air Ventilation": ["Front", "Side"]
}

NUM_ROOMS = 245
NUM_EXTRA = 9

# ---------------
# GENERATING CODE
# ---------------

# Create a file storing all these information
filename = "Stuffs.txt"
f = open(filename, "w")

for i in range(NUM_ROOMS):

    # Create stuffs for the room
    stuffs = MUST_HAVE_STUFFS.copy()
    stuffs += random.sample(EXTRA_STUFFS, NUM_EXTRA)

    # Modify items if there are options in it
    for j in range(len(stuffs)):
        if stuffs[j] in OPTIONAL_ITEMS:
            stuffs[j] = stuffs[j] + " " + random.choice(OPTIONAL_ITEMS[stuffs[j]])

    # Print stuffs out
    f.write(str(i + 1) + ", " + str(stuffs))

f.close()
