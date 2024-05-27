class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [Node() for i in range(10**4)]

    def hash_function(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1        

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        curr = self.map[index]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)