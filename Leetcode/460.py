import unittest
from collections import defaultdict


# Method: List of duble linked lists, direct dictionary reference to key-val node
# Time: O(1) for getting and setting
# Space: O(n)-ish

class Node:
    def __init__(self,
                 key: int, val: int,
                 prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.counter = 1
        self.next = next_node
        self.prev = prev_node


class DoubleLinkedList:

    def __init__(self):
        self.size = 0
        self.sentinel = Node(0, 0)

    def pop(self, node=None) -> Node:
        if self.size == 0:
            raise Exception("Cannot pop from empty double linked list")
        if node is None:  # Pop the tail
            node = self.sentinel.next

        node.next.prev = node.prev
        node.prev.next = node.next

        self.size -= 1
        return node

    def push(self, node: Node):
        if self.size > 0:  # Not empty
            self.sentinel.prev.next = node
            node.prev = self.sentinel.prev
        else:
            self.sentinel.next = node
            node.prev = self.sentinel

        self.sentinel.prev = node
        node.next = self.sentinel
        self.size += 1


class LFUCache:

    def __init__(self, capacity: int):
        self._nodes = {}
        self.capacity = capacity
        self.size = 0
        self._min_freq = 1

        self.dlls = defaultdict(DoubleLinkedList)

    def get(self, key: int) -> int:
        # print(f"Looking for {key}, but I know of {self._nodes}")
        if key not in self._nodes:
            return -1

        node = self._nodes[key]
        self._update_count(node)
        return node.val

    def _update_count(self, node):
        self.dlls[node.counter].pop(node)

        # If was min and now that dll empty, update min
        if self.dlls[node.counter].size == 0 and node.counter == self._min_freq:
            self._min_freq += 1

        node.counter += 1
        self.dlls[node.counter].push(node)

    def put(self, key: int, value: int) -> None:
        # print(f"Putting {key} : {value}, in already ? {key in self._nodes}, size left: {self.capacity - self.size}, min_size {self._min_freq}")
        if self.capacity == 0:
            return

        if key in self._nodes:
            self._nodes[key].val = value
            self._update_count(self._nodes[key])
        else:
            if self.size == self.capacity:
                node = self.dlls[self._min_freq].pop()
                del self._nodes[node.key]
                self.size -= 1
            self._nodes[key] = Node(key, value)
            self.dlls[1].push(self._nodes[key])
            self._min_freq = 1
            self.size += 1


class TestLFU(unittest.TestCase):

    def test_example(self):
        cache = LFUCache(5)
        for i in range(20):
            cache.put(i % 5, i*10)

        for i in range(20):
            print(f" {i} is val: {cache.get(i%5)}")

    def test_lc1(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(2)
        cache.put(3, 3)
        cache.get(2)
        cache.put(4, 4)
        cache.get(1)
        cache.get(3)
        cache.get(4)

    def test_lc2(self):
        cache = LFUCache(3)
        cmds = ["put", "put", "get", "get", "get",
                "put", "put", "get", "get", "get", "get"]
        args = [[2, 2], [1, 1], [2], [1], [2],
                [3, 3], [4, 4], [3], [2], [1], [4]]
        rez = [cache.__getattribute__(cmd)(*arg)
               for cmd, arg in zip(cmds, args)]
        self.assertListEqual(rez, [None, None, 2, 1, 2, None, None, -1, 2, 1, 4])

    def test_midgap_remove(self):
        cache = LFUCache(3)
        cmds = ["put", "put", "put", "put", "put", "get", "get"]
        args = [[10, 10], [10, 10], [10, 10], [3, 30], [3, 40], [10], [2]]
        rez = [cache.__getattribute__(cmd)(*arg)
               for cmd, arg in zip(cmds, args)]
        self.assertListEqual(rez, [None, None, None, None, None, 10, -1])


unittest.main()
