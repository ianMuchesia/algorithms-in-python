class MyHashSet:

    def __init__(self):
       self.hashset = {}

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset[key] = 1
        
        

    def remove(self, key: int) -> None:
        if key in self.hashset:
            del self.hashset[key]
        

    def contains(self, key: int) -> bool:
        return  key in self.hashset
    
class MyHashMap:

    def __init__(self):
        self.hp = {}

    def put(self, key: int, value: int) -> None:
        self.hp[key] = value

    def get(self, key: int) -> int:
        if key in self.hp:
            return self.hp.get(key)
        else:
            return -1
    def remove(self, key: int) -> None:
        if key in self.hp:
            del self.hp[key]
        
    
        