from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key, value):
        if len(self.cache) == self.capacity and key not in self.cache:
            self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(key)

    def __repr__(self):
        return repr(self.cache)

our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.cache)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache
print(our_cache.cache)
our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.cache)
print(our_cache.get(3))

