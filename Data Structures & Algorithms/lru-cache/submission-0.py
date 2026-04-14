class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.head = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.head = Node(0, 0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        # if key not exists, return -1
        if key not in self.map:
            return -1

        # if key in the map -->
            # 1. return value
            # 2. put the key to head
        node = self.map[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key exists already 
        #   --> replace the original value and remove node to head
        if key in self.map:
            # self.map[key] = value
            self.map[key].val = value
            node = self.map[key]
            self._remove(node)
            self._insert_front(node)

        # if key not exists -->
            # 1. put new node to linkedlist's head and the map
            # 2. judege if exceed the capacity, 
                # if exceed: delete the linkedlist's tail and delete from the map
        else:
            node = Node(key, value)
            self.map[key] = node
            # node = self.map[key]
            self._insert_front(node)
            if len(self.map) > self.cap:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.map[lru_node.key]