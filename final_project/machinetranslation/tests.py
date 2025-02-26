import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"),  '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)


    if __name__ == "__main__" :
            unittest.main()
