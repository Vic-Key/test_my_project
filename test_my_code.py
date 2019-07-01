import unittest
from my_code import *

class TestMyCode(unittest.TestCase):

    def test_animal_tail(self):
        self.assertEqual(lion.tail, 1)

    def test_animal_wool(self):
        self.assertTrue(lion.wool)

    def test_dog_tail_incorrect(self):
        self.assertNotEqual(dog.tail, 2)

    def test_dog_tail_correct(self):
        self.assertEqual(dog.tail, 1)

    def test_dog_paw_incorrect(self):
        self.assertNotEqual(dog.paw, 7)

    def test_dog_paw_4(self):
        self.assertEqual(dog.paw, 4)

    def test_dog_wool_correct(self):
        self.assertTrue(dog.wool)

    def test_dog_wool_incorrect(self):
        self.assertFalse(dog.wool)

    def test_say_woof_correct(self):
        self.assertEqual(dog.say_woof(), 'Woof Woof')

    def test_say_woof_incorrect(self):
        self.assertNotEqual(dog.say_woof(), "Meow")

    def test_cat1_tail_correct(self):
        self.assertEqual(cat1.tail, 1)

    def test_cat1_tail_incorrect(self):
        self.assertNotEqual(cat1.tail, 3)

    def test_cat1_paw_correct(self):
        self.assertEqual(cat1.paw, 4)

    def test_cat1_paw_incorrect(self):
        self.assertNotEqual(cat1.paw, 2)

    def test_cat1_wool_correct(self):
        self.assertTrue(cat1.wool)

    def test_cat1_wool_incorrect(self):
        self.assertFalse(cat1.wool)

    def test_say_meow_correct(self):
        self.assertEqual(cat1.say_meow(), "Meow, meow")

    def test_say_meow_incorrect(self):
        self.assertNotEqual(cat1.say_meow(), "Murr")

    def test_sphinx_cat_tail_correct(self):
        self.assertEqual(cat2.tail, 1)

    def test_sphinx_cat_tail_incorrect(self):
        self.assertNotEqual(cat2.tail, 6)

    def test_sphinx_cat_paw_correct(self):
        self.assertEqual(cat2.paw, 4)

    def test_sphinx_cat_paw_incorrect(self):
        self.assertNotEqual(cat2.paw, 5)

    def test_sphinx_cat_wool_correct(self):
        self.assertFalse(cat2.wool)

    def test_sphinx_cat_wool_incorrect(self):
        self.assertTrue(cat2.wool)

    def test_say_murr_correct(self):
        self.assertEqual(cat2.say_murr(), "murr-murr")

    def test_say_murr_incorrect(self):
        self.assertNotEqual(cat2.say_murr(), "Woof")

    def test_rooster_tail_correct(self):
        self.assertEqual(rooster1.tail, 1)

    def test_rooster_tail_incorrect(self):
        self.assertNotEqual(rooster1.tail, 3)

    def test_rooster_paw_correct(self):
        self.assertEqual(rooster1.paw, 2)

    def test_rooster_paw_incorrect(self):
        self.assertNotEqual(rooster1.paw, 4)

    def test_rooster_wool(self):
        self.assertFalse(rooster1.wool)

    def test_rooster_wool_incorrect(self):
        self.assertTrue(rooster1.wool)

    def test_say_cocorico_correct(self):
        self.assertEqual(rooster1.say_Cocorico(), "Cocorico")

    def test_say_cocorico_incorrect(self):
        self.assertNotEqual(rooster1.say_Cocorico(), "Meow")

        