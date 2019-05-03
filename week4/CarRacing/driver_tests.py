import unittest
from car import Car
from driver import Driver

class TestDriver(unittest.TestCase):
    def test_create_valid_driver(self):
        car = Car('Volswagen', 'Passat', 230)
        driver = Driver('Alex', car)

    def test_create_non_valid_driver(self):
        car = 'invalid car'
        with self.assertRaises(TypeError):
            driver = Driver('Alex', car)

    def test_driver_str(self):
        car = Car('Volswagen', 'Passat', 230)
        driver = Driver('Alex', car)
        expected = "Alex Volswagen model Passat max speed: 230"
        self.assertEqual(expected, str(driver))


if __name__ =='__main__':
    unittest.main()