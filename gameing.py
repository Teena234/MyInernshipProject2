class Player:
    def __init__(self):
        self.inventory = []
        self.progress = 0

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def update_progress(self, value):
        self.progress += value


def start_game():
    print("Welcome to the Adventure Game!")
    player = Player()
    # Initialize game variables, story, etc.

    while True:
        # Present the player with choices
        print("You find yourself at a crossroad.")
        print("1. Go left")
        print("2. Go right")
        print("3. Check inventory")
        print("4. Quit")

        choice = input("What do you want to do? Enter your choice: ")

        if choice == "1":
            print("You chose to go left.")
            # Update player progress, story, inventory, etc.
            player.update_progress(1)
        elif choice == "2":
            print("You chose to go right.")
            # Update player progress, story, inventory, etc.
            player.update_progress(2)
        elif choice == "3":
            print("Inventory:")
            print(player.inventory)
        elif choice == "4":
            print("Quitting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    start_game()
