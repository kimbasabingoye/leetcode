class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        for i in range(len(self.data)):
            if self.data[i] == key:
                return
        self.data.append(key)
        

    def remove(self, key: int) -> None:
        i = 0
        n = len(self.data)
        while i < n and self.data[i] != key:
            i += 1
        
        if i != n:
            self.data = self.data[:i] + self.data[i+1:]
            

    def contains(self, key: int) -> bool:
        for i in range(len(self.data)):
            if self.data[i] == key:
                return True
        return False
                


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
