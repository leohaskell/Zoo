import animal
import unittest


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.a = animal.Animal("lion", 24, "sharik", "male", 150)

    def test_animal_init(self):
        self.assertEqual("lion", self.a.species)
        self.assertEqual(24, self.a.age)
        self.assertEqual("sharik", self.a.name)
        self.assertEqual("male", self.a.gender)
        self.assertEqual(150, self.a.weight)

    def test_animal_str(self):
        self.assertEqual("sharik: lion, 24, 150", str(self.a))

    def test_animal_grow(self):
        self.a.grow(250, 7.5)
        self.assertEqual(25, self.a.age)
        self.assertEqual(157.5, self.a.weight)

    def test_animal_grow_above_average(self):
        self.a.grow(150, 5)
        self.assertEqual(25, self.a.age)
        self.assertEqual(150, self.a.weight)

    def test_animal_feed(self):
        result = self.a.feed(0.5)
        self.assertEqual(75, result)

    def test_animal_lives(self):
        result = self.a.lives(1)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
