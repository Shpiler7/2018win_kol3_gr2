import unittest
from flight_simulator import Plane
from flight_simulator import Simulator
import math
#https://github.com/karsta26/kol1_gr2.git

class MyTest(unittest.TestCase):

	def setUp(self):
		self.test_instance = Plane()
		self.test_instance_simulator = Simulator(self.test_instance)

	def test_start_orientation(self):
		self.assertEqual(self.test_instance.orientation, 0)

	def test_max_angle(self):
		self.assertEqual(self.test_instance.max_angle, 270)

	def test_str(self):
		self.assertEqual(str(self.test_instance), "Current orientation: +0.000000\r")

	def test_crash_start(self):
		self.assertEqual(self.test_instance.check_crash(), None)

	def test_if_plane_exists(self):
		self.assertNotEqual(self.test_instance, None)

	def test_if_simulator_exists(self):
		self.assertNotEqual(self.test_instance, None)

	def test_correction_if_greater_than_zero(self):
		new_orientation = 5
		self.test_instance.orientation = new_orientation
		self.test_instance_simulator.apply_tilt_correction()
		self.assertEqual(self.test_instance.orientation, new_orientation-20)

	def test_correction_if_lesser_than_zero(self):
		new_orientation = -5
		self.test_instance.orientation = new_orientation
		self.test_instance_simulator.apply_tilt_correction()
		self.assertEqual(self.test_instance.orientation, new_orientation+20)
	
	def test_correction_if_equal_zero(self):
		self.test_instance_simulator.apply_tilt_correction()
		self.assertEqual(self.test_instance.orientation, 0)

	def test_turbulations(self):
		self.test_instance_simulator.turbulations()
		self.assertNotEqual(self.test_instance.orientation, 0)