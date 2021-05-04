import unittest
import volumeCube

class testVolumeCube(unittest.TestCase):
    def test_neg(self):
        #Passing Test
        self.assertEqual(volumeCube.volume(-1,2,-3), "Invalid Input")
        #Failing Test
        #self.assertEqual(volumeCube.volume(-1,2,-3), "-2")
    def test_zero(self):
        #Passing Test
        self.assertEqual(volumeCube.volume(0,2,0), "Invalid Input")
        #Failing Test
        #self.assertEqual(volumeCube.volume(0,2,0), ".67")
    def test_string(self):
        #Passing Test
        self.assertEqual(volumeCube.volume("a", 1, "asd;kfja"), "Invalid Input")
        #Failing Test
        #self.assertEqual(volumeCube.volume("a", 1, "asd;kfja"), "Good Input")
    



if __name__ == '__main__':
    unittest.main()