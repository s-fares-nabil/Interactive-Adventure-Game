import tkinter as tk
from tkinter import messagebox
from player import create_player, is_alive
from scenes import (
    forest_scene,
    side_quest_scene,
    shop_scene,
    desert_scene,
    companion_scene,
    dungeon_scene,
    castle_scene,
)
from boss import boss_fight
from file_io import read_input_file, write_output_file

# =========================
# GUI CLASS
# =========================
class AdventureGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure RPG")
        self.root.geometry("700x500")

        self.text = tk.Text(root, bg="black", fg="lime", font=("Courier", 12))
        self.text.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.player = None

        self.show_intro()

    # =========================
    def show_text(self, msg):
        self.text.insert(tk.END, msg + "\n")
        self.text.see(tk.END)

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    # =========================
    def show_intro(self):
        self.show_text("WELCOME TO ADVENTURE RPG")
        self.show_text("Enter your name:")

        entry = tk.Entry(self.root)
        entry.pack()

        def start():
            name = entry.get()
            health = read_input_file()
            self.player = create_player(name, health)
            entry.destroy()
            self.start_game()

        tk.Button(self.root, text="Start", command=start).pack()

    # =========================
    def start_game(self):
        self.show_text(f"Welcome, {self.player['name']}!")
        self.forest()

    # =========================
    def forest(self):
        self.show_text("\nForest: A wolf blocks your path.")
        self.clear_buttons()

        tk.Button(self.button_frame, text="Fight",
                  command=lambda: self.forest_choice("A")).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text="Sneak",
                  command=lambda: self.forest_choice("B")).pack(side=tk.LEFT)

    def forest_choice(self, choice):
        if choice == "A":
            self.player["health"] -= 5
            self.player["gold"] += 5
            self.show_text("You fought the wolf (-5 HP, +5 gold)")
        else:
            self.show_text("You sneaked past the wolf.")

        self.side_quest()

    # =========================
    def side_quest(self):
        self.show_text("\nVillage side quest.")
        self.clear_buttons()

        tk.Button(self.button_frame, text="Help Villagers",
                  command=self.help_villagers).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text="Ignore",
                  command=self.ignore_villagers).pack(side=tk.LEFT)

    def help_villagers(self):
        self.player["gold"] += 10
        self.player["inventory"].append("Water Flask")
        self.show_text("You got 10 gold and Water Flask.")
        self.shop()

    def ignore_villagers(self):
        self.show_text("You ignore the villagers.")
        self.shop()

    # =========================
    def shop(self):
        self.show_text("\nMerchant shop.")
        self.clear_buttons()

        tk.Button(self.button_frame, text="Buy Potion (5)",
                  command=self.buy_potion).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text="Buy Sword (10)",
                  command=self.buy_sword).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text="Leave",
                  command=self.desert).pack(side=tk.LEFT)

    def buy_potion(self):
        if self.player["gold"] >= 5:
            self.player["gold"] -= 5
            self.player["inventory"].append("Potion")
            self.show_text("Potion bought.")
        else:
            self.show_text("Not enough gold.")

    def buy_sword(self):
        if self.player["gold"] >= 10:
            self.player["gold"] -= 10
            self.player["attack"] += 3
            self.show_text("Sword bought (+3 attack).")
        else:
            self.show_text("Not enough gold.")

    # =========================
    def desert(self):
        self.show_text("\nCrossing the desert...")
        if "Water Flask" not in self.player["inventory"]:
            self.player["health"] -= 8
            self.show_text("No water! -8 HP")

        if not is_alive(self.player):
            self.end_game("You died in the desert.")
            return

        self.companion()

    # =========================
    def companion(self):
        self.show_text("\nYou meet a wounded knight.")
        self.clear_buttons()

        tk.Button(self.button_frame, text="Help Knight",
                  command=self.help_knight).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text="Ignore",
                  command=self.dungeon).pack(side=tk.LEFT)

    def help_knight(self):
        self.player["companion"] = "Knight"
        self.player["attack"] += 2
        self.show_text("Knight joins you (+2 attack).")
        self.dungeon()

    # =========================
    def dungeon(self):
        self.show_text("\nDungeon entrance...")
        self.player["health"] -= 7
        self.show_text("-7 HP from dungeon fight.")

        if not is_alive(self.player):
            self.end_game("You died in the dungeon.")
            return

        self.castle()

    # =========================
    def castle(self):
        self.show_text("\nFinal Castle...")
        self.show_text("Boss attacks!")

        self.player["health"] -= 10

        if is_alive(self.player):
            self.end_game("YOU WON!")
        else:
            self.end_game("YOU LOST!")

    # =========================
    def end_game(self, msg):
        self.show_text("\n" + msg)
        write_output_file(msg)
        messagebox.showinfo("Game Over", msg)
def animated_button(self, text, command):
    btn = tk.Label(
        self.button_frame,
        text=text,
        bg="darkgreen",
        fg="white",
        font=("Courier", 12),
        padx=20,
        pady=10,
        relief="raised",
        bd=3
    )

    def on_enter(e):
        btn.config(bg="green", fg="black")

    def on_leave(e):
        btn.config(bg="darkgreen", fg="white")

    def on_click(e):
        btn.config(relief="sunken")
        self.root.after(100, command)
        self.root.after(120, lambda: btn.config(relief="raised"))

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", on_click)

    btn.pack(side=tk.LEFT, padx=10, pady=10)


# =========================
# RUN GUI
# =========================
root = tk.Tk()
AdventureGUI(root)
root.mainloop()
