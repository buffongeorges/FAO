from unittest import TestCase
from FAO import Fao


class TestFao(TestCase):
    def setUp(self):
        self.data = Fao()

    def test_countries(self):
        self.assertEqual(self.data.countries()[0], "Afghanistan")

    def test_products(self):
        self.assertEqual(self.data.products("Afghanistan")[0], "Wheat and products")

    def test_min(self):
        self.assertEqual(self.data.min(["Afghanistan"], [2010, 2013]), "a completer")

    def test_max(self):
        self.assertEqual(self.data.max(["Afghanistan"], [2010, 2013]), {'Afghanistan': [['Cereals - Excluding Beer', 'Y2013', 5495], []]})

    def test_av(self):
        self.assertEqual(self.data.av(["Afghanistan"], [1961, 1965], "Wheat and products"), 1889.8)
