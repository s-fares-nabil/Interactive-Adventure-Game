import random

def boss_fight(player):
    """
    Final boss fight - balanced and consistent with the game
    """

    # ===== SAFE DEFAULTS =====
    player.setdefault("flags", {})
    player.setdefault("inventory", [])
    player.setdefault("hp", 100)

    boss_hp = random.randint(45, 60)
    boss_attack = random.randint(7, 12)

    if player["flags"].get("boss_weakness"):
        boss_hp -= 10
        print("You remember the Dark Lord's weakness!")
        print("The boss looks shaken.")

    print("\n=== FINAL BOSS FIGHT ===")
    print("The Dark Lord stands before you.")
    print("There is no escape now.")

    defending = False

    while player["hp"] > 0 and boss_hp > 0:
        print("\nYour turn:")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Potion")
        print("4. Risky Power Attack")
        print("5. Bribe with Gold")

        choice = input("Choose: ")

        # ===== PLAYER TURN =====

        if choice == "1":
            dmg = random.randint(6, 12)
            if "Amulet" in player["inventory"] and random.random() < 0.3:
                dmg *= 2
                print("Critical hit!")
            boss_hp -= dmg
            print(f"You deal {dmg} damage.")

        elif choice == "2":
            defending = True
            print("You brace yourself for the next attack.")

        elif choice == "3":
            if "Potion" in player["inventory"]:
                player["inventory"].remove("Potion")
                heal = random.randint(10, 15)
                player["hp"] += heal
                print(f"You recover {heal} HP.")
            else:
                print("You have no potions!")

        elif choice == "4":
            if random.random() < 0.5:
                dmg = random.randint(15, 25)
                boss_hp -= dmg
                print(f"Power attack successful! {dmg} damage!")
            else:
                backlash = random.randint(5, 10)
                player["hp"] -= backlash
                print(f"Power attack failed! You lose {backlash} HP.")

        elif choice == "5":
            if "Gold" in player["inventory"] and random.random() < 0.3:
                print("The Dark Lord takes the gold and disappears...")
                return "win"
            else:
                print("The Dark Lord rejects your offer!")

        else:
            print("Invalid choice. You hesitate.")

        # ===== BOSS TURN =====
        if boss_hp > 0:
            dmg = random.randint(boss_attack - 2, boss_attack + 3)
            if defending:
                dmg //= 2
                print("Your defense reduces the damage!")
            player["hp"] -= dmg
            print(f"The Dark Lord strikes you for {dmg} damage.")
            defending = False

        # ===== STATUS =====
        print("\nYour HP:", player["hp"])
        print("Boss HP:", boss_hp)

    # ===== RESULT =====
    if player["hp"] > 0:
        print("\nYou have slain the Dark Lord!")
        print("The kingdom is finally free.")
        return "win"
    else:
        print("\nYou fall before the Dark Lord...")
        return "lose"
