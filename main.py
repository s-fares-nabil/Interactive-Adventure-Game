from file_io import read_input_file, write_output_file
from player import create_player, is_alive
from scenes import (
    game_intro,
    forest_scene,
    shop_scene,
    desert_scene,
    dungeon_scene,
    side_quest_scene,
    companion_scene,
    castle_scene,
)
from boss import boss_fight


def print_separator():
    print("=" * 50)


def show_status(player):
    print("\nPLAYER STATUS")
    print("Name:", player["name"])
    print("Health:", player["health"])
    print("Gold:", player["gold"])
    print("Attack:", player["attack"])
    print("Inventory:", player["inventory"])
    if player["companion"]:
        print("Companion:", player["companion"])
    print_separator()


def main():
    game_intro()

    name = input("Enter your name: ")
    health = read_input_file()

    player = create_player(name, health)

    player.setdefault("inventory", [])
    player.setdefault("gold", 10)
    player.setdefault("attack", 5)
    player.setdefault("companion", None)

    print_separator()
    print("WELCOME TO THE ADVENTURE GAME")
    print_separator()

    show_status(player)

    forest_scene(player)
    show_status(player)

    side_quest_scene(player)
    shop_scene(player)

    desert_scene(player)
    if not is_alive(player):
        write_output_file("Player died in the desert.")
        print("You died in the desert.")
        return

    companion_scene(player)
    dungeon_scene(player)

    if not is_alive(player):
        write_output_file("Player died in the dungeon.")
        print("You died in the dungeon.")
        return

    castle_scene(player)
    result = boss_fight(player)

    if result == "win":
        ending = "You won the game!"
        print("VICTORY!")
    else:
        ending = "You lost the game."
        print("DEFEAT!")

    write_output_file(ending)


if __name__ == "__main__":
    main()
