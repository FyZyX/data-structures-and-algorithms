class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Bucket:
    pass


class HashMap:
    def __init__(self):
        self.buckets = []
        self._count = 0

    def insert(self, item: Item):
        self._count += 1

        if self._count > len(self.buckets):
            self._resize()

        # TODO: Add new item to buckets

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
