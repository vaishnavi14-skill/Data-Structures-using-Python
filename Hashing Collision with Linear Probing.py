class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return key % self.size
    def insert(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash Table is full! Cannot insert key:", key)
                return
        self.table[index] = key
        print(f"Key {key} inserted at index {index}.")
    def display(self):
        print("Hash Table:")
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")
# Example usage:
if __name__ == "__main__":
    ht = HashTable(7)
    ht.insert(10)
    ht.insert(20)
    ht.insert(5)
    ht.insert(15)
    ht.insert(33)
    ht.display()
