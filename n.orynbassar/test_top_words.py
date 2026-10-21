
import unittest
from top_words import top_words


class TestTopWords(unittest.TestCase):

    def test_basic_counting(self):
        self.assertEqual(
            top_words("Toyota BMW Toyota Audi BMW Toyota"),
            [("toyota", 3), ("bmw", 2), ("audi", 1)]
        )

    def test_case_insensitive(self):
        self.assertEqual(
            top_words("BMW bmw BMW Mercedes MERCEDES"),
            [("bmw", 3), ("mercedes", 2)]
        )

    def test_punctuation(self):
        self.assertEqual(
            top_words("Toyota, BMW! Toyota. Toyota?"),
            [("toyota", 3), ("bmw", 1)]
        )

    def test_hyphen_separates_words(self):
        self.assertEqual(
            top_words("Mercedes-Benz BMW Mercedes-Benz"),
            [("benz", 2), ("mercedes", 2), ("bmw", 1)]
        )

    def test_alphabetical_tie_breaking(self):
        self.assertEqual(
            top_words("Toyota Honda Ford"),
            [("ford", 1), ("honda", 1), ("toyota", 1)]
        )

    
    def test_limit_ten_words(self):
        result = top_words(
            "Toyota Audi BMW Ford Honda Hyundai Kia Mazda "
            "Nissan Subaru Volvo Mercedes"
        )

        self.assertEqual(len(result), 10)
        self.assertEqual(
            [word for word, count in result],
            [
                "audi", "bmw", "ford", "honda", "hyundai",
                "kia", "mazda", "mercedes", "nissan", "subaru"
            ]
        )

    def test_digits_are_separators(self):
        self.assertEqual(
            top_words("Toyota123 BMW 456 Toyota"),
            [("toyota", 2), ("bmw", 1)]
        )

    def test_empty_text(self):
        self.assertEqual(top_words(""), [])

    def test_punctuation_only(self):
        self.assertEqual(top_words("!!! ... ???"), [])

    def test_russian_and_kazakh(self):
        result = top_words("Алма алма кітап кітап")
        self.assertEqual(
            result,
            [("алма", 2), ("кітап", 2)]
        )

    def test_apostrophe_separates_words(self):
        self.assertEqual(
            top_words("can't can't"),
            [("can", 2), ("t", 2)]
        )


if __name__ == "__main__":
    unittest.main()
