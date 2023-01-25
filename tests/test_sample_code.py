import unittest
import gc

from src.model_inference import ModelInference

class SampleTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.model_object = ModelInference()

    def tearDown(self):
        print('In tearDown()')

    def test_function(self):
        print('in test()')
        self.assertEqual(self.model_object.add(1,2), 3)
    def test_division(self):
        print('in test()')
        self.assertEqual(self.model_object.multiply(1,2), 2)
    def test_substract(self):
        print('in test()')
        self.assertEqual(self.model_object.subtract(1,2), -1)

if __name__ == "__main__":
    unittest.main()