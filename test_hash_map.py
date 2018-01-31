import unittest
from hash_map import Bucket, HashMap, Item


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()
        self.item = Item('key', 'value')

    def test_resize(self):
        self.hash_map.insert(self.item)
        self.assertEqual(len(self.hash_map.buckets), 1)

        self.hash_map.insert(Item('new_key', 'new_value'))
        self.assertEqual(len(self.hash_map.buckets), 2)

    def test_insert(self):
        self.hash_map.insert(self.item)

        self.assertEqual(self.hash_map._count, 1)
        self.assertEqual(len(self.hash_map.buckets), 1)
        self.assertEqual(self.hash_map.buckets[0].next(), self.item)


if __name__ == '__main__':
    unittest.main()
