# =========================
# GAME INTRO
# =========================
def game_intro():
    print(r"""
==================================================
 █████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██║   ██║
███████║██║  ██║██║   ██║
██╔══██║██║  ██║╚██╗ ██╔╝
██║  ██║██████╔╝ ╚████╔╝
╚═╝  ╚═╝╚═════╝   ╚═══╝

        A D V E N T U R E   R P G
==================================================
The land was once peaceful,
until a Dark Lord rose to power.

Fear spread across the kingdom,
and hope began to fade.

You are an adventurer chosen to stop him.

Your goal is clear:
DEFEAT THE DARK LORD.

Choose wisely.
Use your items.
Survive the journey.

The fate of the kingdom is in your hands.
========================================
""")



# =========================
# FOREST
# =========================
def forest_scene(player):
    print("\nLeaving your village behind, you step into the forest.")
    print("The road ahead is dangerous, and the first threat appears.")

    print("A wild wolf blocks your path.")

    print("A) Fight the wolf")
    print("B) Carefully sneak around")

    choice = input("Choose: ").upper()

    if choice == "A":
        player["health"] -= 5
        player["gold"] += 5
        print("You defeat the wolf but lose 5 HP.")
        print("After the fight, you find 5 gold on the ground.")
    else:
        print("You quietly move past the wolf and continue forward.")


# =========================
# SIDE QUEST (VILLAGE)
# =========================
def side_quest_scene(player):
    print("\nAfter surviving the forest, you reach a nearby village.")
    print("The village shows signs of destruction caused by the Dark Lord.")

    print("A villager asks you to help deliver supplies across the desert.")

    print("A) Help the villagers")
    print("B) Refuse and move on")

    choice = input("Choose: ").upper()

    if choice == "A":
        player["gold"] += 10
        player["inventory"].append("Water Flask")
        print("The villagers thank you for your help.")
        print("You receive 10 gold and a Water Flask.")
    else:
        print("You decide not to get involved and continue your journey.")


# =========================
# SHOP
# =========================
def shop_scene(player):
    print("\nAs you leave the village, you meet a traveling merchant.")
    print("Knowing the road ahead is dangerous, you consider buying supplies.")

    print(f"Your gold: {player['gold']}")

    print("A) Buy Potion (5 gold)")
    print("B) Buy Sword (+3 attack, 10 gold)")
    print("C) Leave")

    choice = input("Choose: ").upper()

    if choice == "A" and player["gold"] >= 5:
        player["gold"] -= 5
        player["inventory"].append("Potion")
        print("You buy a Potion and store it in your bag.")
    elif choice == "B" and player["gold"] >= 10:
        player["gold"] -= 10
        player["attack"] += 3
        print("You buy a Sword and feel stronger.")
    else:
        print("You decide to save your gold and move on.")


# =========================
# DESERT
# =========================
def desert_scene(player):
    print("\nThe road from the village leads into a vast desert.")
    print("The sun burns above you as the journey becomes harder.")

    if "Water Flask" in player["inventory"]:
        print("You use the Water Flask to survive the desert heat.")
    else:
        player["health"] -= 8
        print("Without water, the heat exhausts you (-8 HP).")


# =========================
# COMPANION
# =========================
def companion_scene(player):
    print("\nAfter crossing the desert, you reach a crossroads.")
    print("You see a wounded knight fighting the Dark Lord’s scouts.")

    print("A) Help the knight")
    print("B) Ignore and continue")

    choice = input("Choose: ").upper()

    if choice == "A":
        player["companion"] = "Knight"
        player["attack"] += 2
        print("You help the knight defeat the enemies.")
        print("Grateful, he joins you as your companion.")
    else:
        print("You choose not to risk the fight and walk away.")


# =========================
# DUNGEON
# =========================
def dungeon_scene(player):
    print("\nWith your companion by your side, you approach a dark dungeon.")
    print("This dungeon guards the path to the Dark Lord’s castle.")

    print("A) Fight the dungeon monster")
    print("B) Use Potion")
    print("C) Sneak past")

    choice = input("Choose: ").upper()

    if choice == "A":
        player["health"] -= 7
        print("You defeat the monster but lose 7 HP.")
    elif choice == "B" and "Potion" in player["inventory"]:
        player["inventory"].remove("Potion")
        player["health"] += 10
        print("You drink a Potion and recover 10 HP.")
    else:
        print("You carefully sneak past the monster.")


# =========================
# CASTLE
# =========================
def castle_scene(player):
    print("\nBeyond the dungeon, the Dark Lord’s castle rises before you.")
    print("You take a deep breath, knowing this is the final step.")
    print("The final battle awaits...")
