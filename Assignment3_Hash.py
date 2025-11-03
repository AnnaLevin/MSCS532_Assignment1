class HashTableChaining:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.size -= 1
                return True
        return False


# Example test
ht = HashTableChaining()
ht.insert("apple", 10)
ht.insert("banana", 20)
print("apple ->", ht.search("apple"))
ht.delete("apple")
print("apple ->", ht.search("apple"))
