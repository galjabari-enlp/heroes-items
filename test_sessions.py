import unittest
from sessions import Hero

class TestHero(unittest.TestCase):
    def test_inventory_isolation(self):
        conan = Hero("Conan")
        gandalf = Hero("Gandalf")
        
        conan.pick_up_item("Sword of Power")
        
        self.assertIn("Sword of Power", conan.inventory)
        self.assertNotIn("Sword of Power", gandalf.inventory)

if __name__ == '__main__':
    unittest.main()
