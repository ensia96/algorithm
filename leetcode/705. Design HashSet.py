class MyHashSet:

    def __init__(self):
        self.s = 1000
        self.t = [[] for _ in range(self.s)]

    def add(self, key: int) -> None:
        i = key % self.s
        if key not in self.t[i]:
            self.t[i].append(key)

    def remove(self, key: int) -> None:
        i = key % self.s
        if key in self.t[i]:
            self.t[i].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.t[key % self.s]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
