import unittest
from flight_simulator import Plane
import math
#https://github.com/karsta26/kol1_gr2.git

class MyTest(unittest.TestCase):

	def setUp(self):
		self.test_instance = Plane()

	def test_start_orientation(self):
		self.assertEqual(self.test_instance.orientation, 0)

	def test_max_angle(self):
		self.assertEqual(self.test_instance.max_angle, 270)

	def test_str(self):
		self.assertEqual(str(self.test_instance), "Current orientation: +0.000000\r")

	def test_crash_start(self):
		self.assertEqual(self.test_instance.check_crash(), None)