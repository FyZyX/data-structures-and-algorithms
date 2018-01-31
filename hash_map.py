class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"<{repr(self.key)}: {repr(self.value)}>"


class Bucket:
    def __init__(self):
        self._items: [Item] = []

    def insert(self, item: Item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return (item for item in self._items)

    def __repr__(self):
        return repr(self._items)


class HashMap:
    def __init__(self):
        self.buckets = [Bucket()]

    def insert(self, item: Item):
        if len(self) + 1 > len(self.buckets):
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

    def __len__(self):
        return sum(map(lambda bucket: len(bucket), self.buckets))

    def __iter__(self):
        return (item for bucket in self.buckets for item in bucket)
