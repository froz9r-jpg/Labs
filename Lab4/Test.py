import unittest
from Lab4 import ChervonoChorneDerevoCherha

class TestuvanniaCherhy(unittest.TestCase):
    def setUp(self):
        self.cherha = ChervonoChorneDerevoCherha()

    def test_osnovnyi_priorytet(self):
        self.cherha.vstavyty("Zavdannia 1", 5)
        self.cherha.vstavyty("Zavdannia 2", 100)
        self.cherha.vstavyty("Zavdannia 3", 50)
        rezultat = self.cherha.vydalyty_ta_povernuty()
        self.assertEqual(rezultat, ("Zavdannia 2", 100))

    def test_perehliad_bez_vydalennia(self):
        self.cherha.vstavyty("Test", 10)
        self.assertEqual(self.cherha.perehliad(), ("Test", 10))
        self.assertEqual(self.cherha.perehliad(), ("Test", 10))

    def test_porozhnia_cherha(self):
        self.assertIsNone(self.cherha.perehliad())
        self.assertIsNone(self.cherha.vydalyty_ta_povernuty())

    def test_poslidovnist(self):
        dani = [("A", 10), ("B", 40), ("C", 20)]
        for v, p in dani: self.cherha.vstavyty(v, p)
        self.assertEqual(self.cherha.vydalyty_ta_povernuty(), ("B", 40))
        self.assertEqual(self.cherha.vydalyty_ta_povernuty(), ("C", 20))
        self.assertEqual(self.cherha.vydalyty_ta_povernuty(), ("A", 10))

if __name__ == "__main__":
    unittest.main()