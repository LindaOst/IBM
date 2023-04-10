# test_translate.py

import unittest
from translate_pack import translate_english_to_french, translate_french_to_english


class TestTranslateFunctions(unittest.TestCase):

    def test_translate_english_to_french(self):
        english_text = 'Hello, how are you?'
        french_text = translate_english_to_french(english_text)
        self.assertNotEqual(english_text, french_text)
        self.assertIsInstance(french_text, str)

    def test_translate_french_to_english(self):
        french_text = 'Bonjour, comment ça va?'
        english_text = translate_french_to_english(french_text)
        self.assertNotEqual(french_text, english_text)
        self.assertIsInstance(english_text, str)


if __name__ == '__main__':
    unittest.main()
