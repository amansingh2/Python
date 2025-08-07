
class LRUCache:
    def __init__(self , capacity: int):
        self.capacity = capacity
        self.cache = dict()

    def get(self , key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self , key: int , value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) == self.capacity:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value

lru = LRUCache(2)
lru.put(1 , 10)
lru.put(2 , 20)
print(lru.get(2))
lru.put(3 , 30)
print(lru.get(1))