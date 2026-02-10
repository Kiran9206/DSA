# Linear probing....
class Deleted:
    pass


class Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value



class HashMap:


    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size
        self.count = 0
        self.threshold = 0.7

    def _hash(self, key):
        return abs(hash(key)) % self.size


    def insert(self, key, value):
        bucket_idx = self._hash(key)
        entry, idx = self.checkWithInBucket(key, bucket_idx)
        if entry is None:
            new_pair = Pair(key, value)
            self.bucket[idx] = new_pair
            self.count += 1
        else:
            entry.value = value

        if (self.count / self.size) > self.threshold:
            self.rehash()


    def get(self, key):
        bucket_idx = self._hash(key)
        entry, idx = self.checkWithInBucket(key, bucket_idx)
        if entry is None:
            return None
        return entry.value

    def remove(self, key):
        bucket_idx = self._hash(key)
        entry, idx = self.checkWithInBucket(key, bucket_idx)
        if entry is None:
            return -1
        self.bucket[idx] = Deleted()
        self.count-=1
        return


    def checkWithInBucket(self, key, bucket_idx):
        while True:
            if self.bucket[bucket_idx] is None:
                return None,bucket_idx
            if isinstance(self.bucket[bucket_idx], Pair) and self.bucket[bucket_idx].key == key:
                return self.bucket[bucket_idx], bucket_idx
            bucket_idx = (bucket_idx + 1) % self.size

    def rehash(self):
        old_bucket = self.bucket
        self.size = 2 * self.size
        self.count = 0
        self.bucket = [None] * self.size
        for idx in range(len(old_bucket)):
            if old_bucket[idx] is not None:
                if isinstance(old_bucket[idx], Pair):
                    self.insert(old_bucket[idx].key, old_bucket[idx].value)
# ----------------------------------------------------------------------------------------------------------------------


