import unittest
import volumeCube

class testVolumeCube(unittest.TestCase):
    def test_neg(self):
        self.assertEqual(volumeCube.volume(-1,2,-3), "Invalid Input")
    def test_zero(self):
        self.assertEqual(volumeCube.volume(0,2,0), "Invalid Input")
    def test_string(self):
        self.assertEqual(volumeCube.volume("a", 1, "asd;kfja"), "Invalid Input")
    



if __name__ == '__main__':
    unittest.main()