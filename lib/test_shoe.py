import unittest
from shoe import Shoe  

class TestShoe(unittest.TestCase):
    def test_shoe_creation(self):
        shoe = Shoe("Nike", 10, "Black")
        self.assertEqual(shoe.brand, "Nike")
        self.assertEqual(shoe.size, 10)
        self.assertEqual(shoe.color, "Black")
        self.assertFalse(shoe.is_worn)

    def test_wear_shoe(self):
        shoe = Shoe("Nike", 10, "Black")
        shoe.wear()
        self.assertTrue(shoe.is_worn)

    def test_take_off_shoe(self):
        shoe = Shoe("Nike", 10, "Black")
        shoe.wear()
        shoe.take_off()
        self.assertFalse(shoe.is_worn)

    def test_already_wearing_shoe(self):
        shoe = Shoe("Nike", 10, "Black")
        shoe.wear()
        
        # Capture the print output to check what's printed
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        shoe.wear()
        
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        
        self.assertIn("You are already wearing these shoes.", output)

if __name__ == '__main__':
    unittest.main()
