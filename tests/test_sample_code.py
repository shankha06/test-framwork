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
        self.assertEqual(self.add(1,2), 3)