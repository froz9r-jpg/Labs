import unittest
from Lab2 import znayty_maksymalnu_kilkist

class TestKhomyachky(unittest.TestCase):
    def test_pryklad_1(self):
        self.assertEqual(znayty_maksymalnu_kilkist(7, 3, [[1,2],[2,2],[3,1]]), 2)
    def test_pryklad_2(self):
        self.assertEqual(znayty_maksymalnu_kilkist(19, 4, [[5,0],[2,2],[1,4],[5,1]]), 3)
    def test_pryklad_3(self):
        self.assertEqual(znayty_maksymalnu_kilkist(2, 2, [[1,50000],[1,60000]]), 1)
    def test_pryklad_4(self):
       self.assertEqual(znayty_maksymalnu_kilkist(33, 3, [[1,2],[3,4],[5,6]]), 3)
if __name__ == '__main__':
    unittest.main()