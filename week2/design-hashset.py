class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.a = [[] for i in range(self.size)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.a[self.hash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.a[self.hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        for i, k in enumerate(self.a[self.hash(key)]): 
            if k == key:
                return True
        return False
    def hash(self, key):
        return (key & 0x7FFFFFFF) % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)