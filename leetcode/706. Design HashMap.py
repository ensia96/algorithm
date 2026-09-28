class MyHashMap:

    def __init__(self):
        self.s = 1000
        self.m = [[] for _ in range(self.s)]

    def put(self, key: int, value: int) -> None:
        i = key % self.s
        for j, (k, _) in enumerate(self.m[i]):
            if k == key:
                self.m[i][j] = (key, value)
                return
        self.m[i].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.m[key % self.s]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        i = key % self.s
        for j, (k, _) in enumerate(self.m[i]):
            if k == key:
                del self.m[i][j]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
