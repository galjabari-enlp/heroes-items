import unittest
from sessions import Hero


class TestHero(unittest.TestCase):
    """Test cases for the Hero class to prevent mutable default argument bug."""

    def test_heroes_have_independent_inventories(self):
        """Test that each Hero instance has its own independent inventory."""
        conan = Hero("Conan")
        gandalf = Hero("Gandalf")

        # Conan picks up an item
        conan.pick_up_item("Sword of Power")

        # Verify Conan has the item
        self.assertEqual(conan.inventory, ["Sword of Power"])

        # Verify Gandalf's inventory is empty (not affected by Conan's action)
        self.assertEqual(gandalf.inventory, [])

    def test_multiple_heroes_multiple_items(self):
        """Test that multiple heroes can have different items independently."""
        conan = Hero("Conan")
        gandalf = Hero("Gandalf")
        aragorn = Hero("Aragorn")

        conan.pick_up_item("Sword of Power")
        gandalf.pick_up_item("Staff of Wisdom")
        aragorn.pick_up_item("Anduril")

        self.assertEqual(conan.inventory, ["Sword of Power"])
        self.assertEqual(gandalf.inventory, ["Staff of Wisdom"])
        self.assertEqual(aragorn.inventory, ["Anduril"])

    def test_hero_with_initial_inventory(self):
        """Test that a hero can be created with an initial inventory."""
        initial_items = ["Potion", "Map"]
        hero = Hero("Lara", initial_items)

        self.assertEqual(hero.inventory, initial_items)

    def test_initial_inventory_not_shared(self):
        """Test that initial inventory passed to one hero doesn't affect others."""
        shared_list = ["Potion"]
        hero1 = Hero("Hero1", shared_list)
        hero2 = Hero("Hero2")

        hero1.pick_up_item("Sword")

        # hero1 should have both items
        self.assertEqual(hero1.inventory, ["Potion", "Sword"])
        # hero2 should have empty inventory
        self.assertEqual(hero2.inventory, [])

    def test_empty_inventory_by_default(self):
        """Test that a new hero has an empty inventory by default."""
        hero = Hero("NewHero")
        self.assertEqual(hero.inventory, [])


if __name__ == "__main__":
    unittest.main()