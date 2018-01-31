import unittest
from hash_map import Bucket, HashMap, Item


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.item = Item('key', 'value')

    def test_insert(self):
        hash_map = HashMap()
        hash_map.insert(self.item)

        self.assertEqual(hash_map._count, 1)
        self.assertEqual(len(hash_map.buckets), 1)
        self.assertEqual(hash_map.buckets[0].next(), self.item)


if __name__ == '__main__':
    unittest.main()
