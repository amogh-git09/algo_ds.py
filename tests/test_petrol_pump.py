import unittest
from algo_ds.petrol_pump import *
from algo_ds.queue import Queue

class TestPetrolPumpStart(unittest.TestCase):
    def test_find_start(self):
        petrol_pumps = [(4,6), (6,5), (7,3), (4,5)]
        self.assertIn(find_start(petrol_pumps), (1, 2))
        petrol_pumps = [(4,6), (6,5), (7,8), (4,4)]
        self.assertEqual(find_start(petrol_pumps), -1)
        petrol_pumps = [(4,6), (6,5), (7,3), (4,5), (0,4)]
        self.assertEqual(find_start(petrol_pumps), -1)
        petrol_pumps = [(4,6), (6,7), (7,3), (9,5), (0,4)]
        self.assertEqual(find_start(petrol_pumps), 2)

    def test_find_start_linked_queue(self):
        petrol_pumps = Queue()
        petrol_pumps.enqueue(PetrolPump(4,6))
        petrol_pumps.enqueue(PetrolPump(6,5))
        petrol_pumps.enqueue(PetrolPump(7,3))
        petrol_pumps.enqueue(PetrolPump(4,5))
        self.assertEqual(str(find_start_linked_queue(petrol_pumps)), str(PetrolPump(6,5)))

        petrol_pumps = Queue()
        petrol_pumps.enqueue(PetrolPump(4,6))
        petrol_pumps.enqueue(PetrolPump(6,5))
        petrol_pumps.enqueue(PetrolPump(7,8))
        petrol_pumps.enqueue(PetrolPump(4,4))
        self.assertEqual(find_start_linked_queue(petrol_pumps), None)

        petrol_pumps = Queue()
        petrol_pumps.enqueue(PetrolPump(4,6))
        petrol_pumps.enqueue(PetrolPump(6,7))
        petrol_pumps.enqueue(PetrolPump(7,3))
        petrol_pumps.enqueue(PetrolPump(9,5))
        petrol_pumps.enqueue(PetrolPump(0,4))
        self.assertEqual(str(find_start_linked_queue(petrol_pumps)), str(PetrolPump(7,3)))
