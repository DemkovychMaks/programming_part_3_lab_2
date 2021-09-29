import unittest
from main import Deque


class TestDeque(unittest.TestCase):

    def test_insert_front(self):
        my_deque = Deque()
        my_deque.insert_front(20)
        my_deque.insert_front(30)
        my_deque.insert_front(40)
        my_deque.insert_front(50)
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [50, 40, 30, 20])

    def test_insert_last(self):
        my_deque = Deque()
        my_deque.insert_rear(20)
        my_deque.insert_rear(30)
        my_deque.insert_rear(40)
        my_deque.insert_rear(50)
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [20, 30, 40, 50])

    def test_delete_front(self):
        my_deque = Deque()
        my_deque.insert_rear(20)
        my_deque.insert_rear(30)
        my_deque.insert_rear(40)
        my_deque.insert_rear(50)
        my_deque.delete_front()
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [30, 40, 50])

    def test_delete_last(self):
        my_deque = Deque()
        my_deque.insert_front(20)
        my_deque.insert_front(30)
        my_deque.insert_front(40)
        my_deque.insert_front(50)
        my_deque.delete_last()
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [50, 40, 30])

    def test_get_front(self):
        my_deque = Deque()
        my_deque.insert_front(20)
        my_deque.insert_front(30)
        my_deque.insert_front(40)
        my_deque.insert_front(50)
        self.assertEqual(my_deque.get_front(), 50)

    def test_get_last(self):
        my_deque = Deque()
        my_deque.insert_front(20)
        my_deque.insert_front(30)
        my_deque.insert_front(40)
        my_deque.insert_front(50)
        self.assertEqual(my_deque.get_last(), 20)