class Hero:
    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = inventory if inventory is not None else []

    def pick_up_item(self, item):
        print(f"{self.name} picked up: {item}")
        self.inventory.append(item)

    def show_inventory(self):
        print(f"{self.name}'s Backpack: {self.inventory}")

conan = Hero("Conan")


gandalf = Hero("Gandalf")


conan.pick_up_item("Sword of Power")


conan.show_inventory()
gandalf.show_inventory()