class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head, self.tail = None, None
        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.__move_node_to_end(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.__move_node_to_end(node)
            return
        
        node = LRUNode(key=key, val=value)
        self.cache[key] = node
        if self.count == self.capacity:
            self.__evict_lru_head()
        else:
            self.count += 1
        
        if self.head is None:
            self.head = self.tail = node
        else:
            self.__move_node_to_end(node)
        
    def __evict_lru_head(self):
        if self.head:
            del self.cache[self.head.key]
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            self.count -= 1
    
    def __move_node_to_end(self, node: LRUNode):
        if node == self.tail:
            return
        
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        node.next = None

        if self.head is None:
            self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)