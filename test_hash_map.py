import unittest
from hash_map import Bucket, HashMap, Item


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()
        self.item = Item('key', 'value')

    def test_resize(self):
        self.assertEqual(len(self.hash_map.buckets), 1)
        self.hash_map._resize()
        self.assertEqual(len(self.hash_map.buckets), 2)
        self.hash_map._resize()
        self.assertEqual(len(self.hash_map.buckets), 4)

    def test_insert(self):
        self.hash_map.insert(self.item)

        self.assertEqual(len(self.hash_map), 1)
        self.assertEqual(len(self.hash_map.buckets), 1)
        self.assertIn(self.item, self.hash_map)

        new_item_1 = Item('new key', 'new value')
        self.hash_map.insert(new_item_1)

        self.assertEqual(len(self.hash_map), 2)
        self.assertEqual(len(self.hash_map.buckets), 2)
        self.assertIn(self.item, self.hash_map)
        self.assertIn(new_item_1, self.hash_map)

        new_item_2 = Item('newer key', 'newer value')
        self.hash_map.insert(new_item_2)

        self.assertEqual(len(self.hash_map), 3)
        self.assertEqual(len(self.hash_map.buckets), 4)
        self.assertIn(self.item, self.hash_map)
        self.assertIn(new_item_1, self.hash_map)
        self.assertIn(new_item_2, self.hash_map)


if __name__ == '__main__':
    unittest.main()
