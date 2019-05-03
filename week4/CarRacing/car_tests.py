import unittest
from car import Car

class TestCar(unittest.TestCase):
    def test_create_valid_car(self):
        car = Car('Volswagen', 'Passat', 230)

    def test_create_car_with_invalid_speed(self):
        with self.assertRaises(AssertionError):
            car = Car('VW', 'Passat', 'NaN')

    def test_car_str(self):
        car = Car('Volswagen', 'Passat', 230)
        expected = "Volswagen model Passat max speed: 230"
        self.assertEqual(expected, str(car))


if __name__ =='__main__':
    unittest.main()