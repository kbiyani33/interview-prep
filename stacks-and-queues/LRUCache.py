class DoublyLinkedListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        dummyHead, dummyTail = DoublyLinkedListNode(-1, -1), DoublyLinkedListNode(-1, -1)
        dummyHead.next = dummyTail
        dummyTail.prev = dummyHead
        self.head, self.tail = dummyHead, dummyTail
        self.nodemap = {}
    
    def insertAfterHead(self, node:DoublyLinkedListNode) -> None:
        nextToHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextToHead
        nextToHead.prev = node
    
    def deleteBeforeTail(self) -> DoublyLinkedListNode:
        tail = self.tail
        prevToTail = tail.prev
        prevToPrevToTail = prevToTail.prev
        prevToPrevToTail.next = tail
        tail.prev = prevToPrevToTail
        return prevToTail

    def get(self, key: int) -> int:
        node = self.nodemap.get(key, None)
        if node:
            nextToNode = node.next
            prevToNode = node.prev
            prevToNode.next = nextToNode
            nextToNode.prev = prevToNode
            self.insertAfterHead(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        nodemap = self.nodemap
        node = nodemap.get(key, None)
        if node:
            node.val = value
            nextToNode = node.next
            prevToNode = node.prev
            prevToNode.next = nextToNode
            nextToNode.prev = prevToNode
        else:
            node = DoublyLinkedListNode(key=key, val=value)
            nodemap[key] = node
        self.insertAfterHead(node)
        # now simply check if capacity is overflowing
        if len(nodemap) > self.capacity:
            deleted = self.deleteBeforeTail()
            del nodemap[deleted.key]
    






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)