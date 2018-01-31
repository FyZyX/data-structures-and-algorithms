class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Bucket:
    def __init__(self):
        self._items: [Item] = []
        self._current = -1

    def insert(self, item: Item):
        self._items.append(item)

    def next(self):
        self._current += 1
        return self._items[self._current]


class HashMap:
    def __init__(self):
        self.buckets = [Bucket()]
        self._count = 0

    def insert(self, item: Item):
        self._count += 1

        if self._count > len(self.buckets):
            self._resize()

        bucket = self.buckets[hash(item.key) % len(self.buckets)]
        bucket.insert(item)

    def delete(self, key):
        pass

    def get(self, key):
        pass

    def _resize(self):
        scale = 2
        # Save old items and reset buckets
        old_buckets, self.buckets = self.buckets, []

        # Increase the number of buckets by the scale factor
        [self.buckets.append(Bucket()) for _ in range(len(old_buckets) * scale)]

        # Insert each item in a new bucket
        [self.insert(item) for bucket in old_buckets for item in bucket]
