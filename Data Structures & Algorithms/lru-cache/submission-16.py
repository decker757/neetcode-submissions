class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right

    def remove(self, node):
        self.prev, self.nxt = node.prev, node.next
        self.prev.next, self.nxt.prev = self.nxt, self.prev

    def insert(self, node):
        self.prev, self.nxt = self.right.prev, self.right
        self.prev.next = self.nxt.prev = node
        node.prev, node.next = self.prev, self.nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
