
class Pair:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class Hash_map:


    def __init__(self, size=10,threshold=2.0):
        self.size = size
        self.bucket = [None] * self.size
        self.count = 0
        self.threshold =threshold


    def searchWithinBucket(self, key, bucket_idx):
        curr = self.bucket[bucket_idx]
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def insert(self, key, value):
        # steps:
            # find the bucket index by hashing
            # search a key in the bucket
                # if key present update the value
                # if not add the value in the bucket linked list
        bucket_idx = abs(key) % self.size
        existing_node = self.searchWithinBucket(key, bucket_idx)
        if existing_node is None:
            new_node = Pair(key, value)
            new_node.next = self.bucket[bucket_idx]
            self.bucket[bucket_idx] = new_node
            self.count+=1
        else:
            existing_node.value = value

        if (self.count / self.size) > self.threshold:
            self.rehash()

    def get(self, key):
        bucket_idx = abs(key) % self.size
        existing_node = self.searchWithinBucket(key, bucket_idx)
        if existing_node is None:
            return None
        return existing_node.value

    def remove(self, key):
        bucket_idx = abs(key) % self.size
        existing_node = self.searchWithinBucket(key, bucket_idx)
        if existing_node is None:
            return
        curr = self.bucket[bucket_idx]
        prev = None
        while curr:
            if curr.key == key:
                self.count-=1
                if prev is None: # which means we are at head node
                    self.bucket[bucket_idx] = curr.next
                    return
                else: # we are in middle or end node
                    prev.next = curr.next  #bypassing....
                    return
            prev = curr
            curr = curr.next


    def rehash(self):
        old_buck = self.bucket
        self.size = self.size * 2
        self.bucket = [None] * self.size
        self.count = 0
        for head in old_buck:
            curr = head
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next


