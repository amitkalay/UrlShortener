import unittest
from resources.ShortenUrl import ShortenUrl


class TestGenerateUrl(unittest.TestCase):

    def test_gen_url(self):
        short_url = ShortenUrl.generate_short_url(ShortenUrl(), 6)
        self.assertEqual(6, len(short_url))


if __name__ == '__main__':
    unittest.main()